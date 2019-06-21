import json
import csv


def process():
    with open('jobs.json') as json_file:
        data = json.load(json_file)
        with open('it_bosch_jobs.csv', 'a') as writeFile:
            writer = csv.writer(writeFile)
            for p in data['hits']['hits']:
                if 'Arch' in p['_source']['name']:
                    print(p['_id'] + ', ' + p['_source']['releasedDate'] + ',' + p['_source']['name'] + ',' + p['_source']['applyUrl'] + ',')
                    writer.writerow([p['_id'], p['_source']['releasedDate'], p['_source']['name'], p['_source']['applyUrl']])
        writeFile.close()


if __name__ == '__main__':
    process()