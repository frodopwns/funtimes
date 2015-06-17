from datetime import datetime, timedelta

class RaceAverage(object):

    def __init__(self):
        pass

    def avgMinutes(self, strings):
        start = datetime.strptime('08:00 AM', '%H:%M %p')

        total = 0
        count = 0
        for s in strings:
            time_string, day = s.split(", ")
            day = int(day[4:]) - 1
            if day == 0:
                diff = datetime.strptime(time_string, '%H:%M %p') - start
                diff += timedelta(days=day)
                minutes = divmod(diff.total_seconds(), 60)[0]
            else:
                minutes = 960
                for i in range(day):

                    if i+1 == len(range(day)):
                        if time_string[-2:] == "AM":
                            if time_string[:2] == "12":
                                delta = 0
                            else:
                                delta = int(time_string[:2]) * 60
                        else:
                            delta = (12 * 60) + (int(time_string[:2]) * 60)
                        minutes += delta + int(time_string[3:5])
                    else:
                        minutes += 1440

            total += int(round(minutes))
            count += 1

        return int(round(total / float(count)))


if __name__ == '__main__':
    test_data = [
        ["12:00 PM, DAY 1", "12:01 PM, DAY 1"],
        ["12:00 AM, DAY 2"],
        ["02:00 PM, DAY 19", "02:00 PM, DAY 20", "01:58 PM, DAY 20"],
    ]
    answers = [241, 960, 27239]
    race = RaceAverage()
    for i, test in enumerate(test_data):
        print "running test with data: [%s]" % ", ".join(["'%s'" % x for x in test])
        v = race.avgMinutes(test)
        assert(v == answers[i])
        print "average: %d" % v
        print "Success!"




