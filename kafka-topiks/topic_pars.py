### kafka 2.8 

import subprocess
import yaml
import argparse
#############
parser = argparse.ArgumentParser()
parser.add_argument("--kafka_home", help="path to kafka home directory")
parser.add_argument("--bootstrap_server", help="ip:port of bootstrap-server")
parser.add_argument("--zookeeper_server", help="ip:port of zookeeper")
parser.add_argument("--cluster_suffix", help="qa, dev, demo, prod, etc")
parser.add_argument("--migrate", help="update or recreate")
parser.add_argument("--delete", help="update or recreate")
parser.add_argument("--recreate", help="update or recreate")
args = parser.parse_args()


kafka_home = '/home/user/Documents/kafka_2.12-2.8.0'
kafka_config = kafka_home + '/bin/kafka-configs.sh'
kafka_topics = kafka_home + '/bin/kafka-topics.sh'
bootstrap_server = '192.168.1.41:9092'
zookeeper_server = '192.168.1.41:2181'
cluster_suffix = 'dev'
migrate = 'update'
recreate = 'all'
delete = 'no'

if args.kafka_home:
    print(args.kafka_home)
    kafka_home = args.kafka_home
if args.bootstrap_server:
    bootstrap_server = args.bootstrap_server
if args.zookeeper_server:
    zookeeper_server = args.zookeeper_server
if args.cluster_suffix:
    cluster_suffix = args.cluster_suffix
if args.migrate:
    migrate = args.migrate
if args.delete == 'yes':
    delete = args.delete
if args.migrate and args.recreate:
    recreate = args.recreate
print('delete topics? ', delete)
#############








def parseYaml():
    with open('./topics.yaml') as f:
        topics = yaml.load(f, Loader=yaml.FullLoader)
    for topic in topics:
        topic['Topic'] = topic['Topic'] + '-' + cluster_suffix
    return topics



def describeTopics():
    
    topicsList = subprocess.check_output([kafka_topics, '--bootstrap-server', bootstrap_server, '--describe'])

    if topicsList != b'':
        topicsListNew = []
        
        topicsList = topicsList[:-1]
        topicsList = topicsList.decode().split('\n')
        
        for i in topicsList:
            if isinstance(i, str):
                i = i.split('\t')

            else:
                print("ooooops!!")            
        
        for i in  range(0, len(topicsList)):
            if topicsList[i][0] != "\t":
                topicsListNew.append(topicsList[i])


        for n, i in enumerate(topicsListNew):
            topicsListNew[n] = dict(map(lambda x: x.split(': '), i.split('\t')))
            topicsListNew[n]['Configs'] = dict(map(lambda x: x.split('='), topicsListNew[n]['Configs'].split(',')))
        return topicsListNew

    else: 
        print("no current topics")
        return topicsList
    

def compareLists(importedTopics, describeTopics):

    if describeTopics != b'':
        for topic in importedTopics:
            for existedTopic in describeTopics:
                if topic['Topic'] == existedTopic['Topic']:

                    topic['exists'] = True

                    if topic['partitions'] != int(existedTopic['PartitionCount']):
                        topic['partitions-update'] = True

                    if topic['replication-factor'] != int(existedTopic['ReplicationFactor']):
                        topic['replication-factor-update'] = True

                    if 'retention.ms' in existedTopic['Configs'].keys():
                        if topic['config']['retention.ms'] != int(existedTopic['Configs']['retention.ms']):
                            topic['config']['retention-ms-update'] = True
                    else:
                        topic['config']['retention-ms-update'] = True

    return importedTopics


def createTopics(resultListOfTopics):
    for topic in importedTopics:
        if topic['exists'] == False:
            retentionMs = 'retention.ms=' + str(topic['config']['retention.ms'])
            subprocess.call([kafka_topics, '--bootstrap-server', bootstrap_server, 
            '--if-not-exists', '--create', 
            '--topic', topic['Topic'], 
            '--replication-factor', str(topic['replication-factor']),
            '--partitions', str(topic['partitions']),
            '--config', retentionMs])



def deleteTopics(resultListOfTopics):
    for topic in resultListOfTopics:
        subprocess.call([kafka_topics, '--bootstrap-server', bootstrap_server, '--delete', '--topic', topic['Topic']])



def updateTopics(resultListOfTopics):

    ####update replication-factor and partitions
    
    for topic in resultListOfTopics:
               
        if  topic['exists'] == True and (topic['partitions-update'] == True or topic['replication-factor-update'] == True):
            subprocess.run([kafka_topics, '--bootstrap-server', bootstrap_server, 
            '--alter', '--topic', topic['Topic'], 
            '--partitions', str(topic['partitions']),
            'replication-factor', str(topic['replication-factor']) ])
        
        if topic['exists'] == True and topic['config']['retention-ms-update'] == True:
            retentionMs = 'retention.ms=' + str(topic['config']['retention.ms'])
            subprocess.run([kafka_config, '--bootstrap-server', bootstrap_server, #'--zookeeper', zookeeper_server, 
            '--alter', '-entity-type', 'topics','--entity-name', topic['Topic'], 
            '--add-config', retentionMs ])


def recreateTopics(resultListOfTopics):

    if recreate == 'all':
        for topic in resultListOfTopics:
            if topic['exists'] == True:
                retentionMs = 'retention.ms=' + str(topic['config']['retention.ms'])
                subprocess.call([kafka_topics, '--bootstrap-server', bootstrap_server, '--delete', '--topic', topic['Topic']])
                subprocess.call([kafka_topics, '--bootstrap-server', bootstrap_server, 
                '--if-not-exists', '--create', 
                '--topic', topic['Topic'], 
                '--replication-factor', str(topic['replication-factor']),
                '--partitions', str(topic['partitions']),
                '--config', retentionMs])
    elif recreate == 'changed':
        for topic in resultListOfTopics:
            if  topic['exists'] == True and (topic['partitions-update'] == True or topic['replication-factor-update'] == True):
                retentionMs = 'retention.ms=' + str(topic['config']['retention.ms'])
                subprocess.call([kafka_topics, '--bootstrap-server', bootstrap_server, '--delete', '--topic', topic['Topic']])
                subprocess.call([kafka_topics, '--bootstrap-server', bootstrap_server, 
                '--if-not-exists', '--create', 
                '--topic', topic['Topic'], 
                '--replication-factor', str(topic['replication-factor']),
                '--partitions', str(topic['partitions']),
                '--config', retentionMs])
    else:
        topic = resultListOfTopics[recreate]
        if  topic['exists'] == True and (topic['partitions-update'] == True or topic['replication-factor-update'] == True):
            retentionMs = 'retention.ms=' + str(topic['config']['retention.ms'])
            subprocess.call([kafka_topics, '--bootstrap-server', bootstrap_server, '--delete', '--topic', topic['Topic']])
            subprocess.call([kafka_topics, '--bootstrap-server', bootstrap_server, 
            '--if-not-exists', '--create', 
            '--topic', topic['Topic'], 
            '--replication-factor', str(topic['replication-factor']),
            '--partitions', str(topic['partitions']),
            '--config', retentionMs])

       
def migrateTopics(resultListOfTopics):
   
    ##############
    #Create non-existed topics
    createTopics(resultListOfTopics)

    ##############
    #Update or recreate existed topics

    if migrate == 'update':
        updateTopics(resultListOfTopics)
    elif migrate == 'recreate':
        recreateTopics(resultListOfTopics[])


importedTopics = parseYaml()
describeTopics = describeTopics()
resultListOfTopics = compareLists(importedTopics, describeTopics)

if delete == 'no':
    migrateTopics(resultListOfTopics)
elif delete == 'yes':
    deleteTopics(describeTopics)
else:
    print("Wrong delete argument")



