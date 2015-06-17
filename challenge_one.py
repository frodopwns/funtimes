from datetime import datetime, timedelta

class RaceAverage(object):

    def __init__(self):
        pass

    def avgMinutes(self, strings):
        """
        Receives a list of strings like ["12:00 PM, DAY 1", "12:01 PM, DAY 1"]
        and calculates an average time in minutes from when the race started
        at 8am on Day 1.

        """
        # start of race
        start = datetime.strptime('08:00 AM', '%H:%M %p')

        total = 0
        count = 0
        for s in strings:
            time_string, day = s.split(", ")
            day = int(day[4:]) - 1
            # if these racers finished the day of the race
            if day == 0:
                diff = datetime.strptime(time_string, '%H:%M %p') - start
                diff += timedelta(days=day)
                minutes = divmod(diff.total_seconds(), 60)[0]
            else:
                # time from the rest of the first day
                minutes = 960
                # loop through the additional days
                for i in range(day):
                    # check if last day
                    if i+1 == len(range(day)):
                        if time_string[-2:] == "AM":
                            if time_string[:2] == "12":
                                delta = 0
                            else:
                                delta = int(time_string[:2]) * 60
                        else:
                            delta = (12 * 60) + (int(time_string[:2]) * 60)
                        # add the minutes from the last day
                        minutes += delta + int(time_string[3:5])
                    else:
                        # add 24 hours worth of minutes for each full day
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




