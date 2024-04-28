
class Solution:
    def reformatDate(self, date: str) -> str:
        monthToNumber = {"Jan": '01', "Feb": '02', "Mar": '03', "Apr": '04', "May": '05', "Jun": '06', "Jul": '07',
                         "Aug": '08', "Sep": '09', "Oct": '10', "Nov": '11', "Dec": '12'}
        day, month, year = date.split(' ')
        ans = [year, monthToNumber[month]]
        if len(day) == 3:
            ans.append('0' + day[:len(day) - 2])
        else:
            ans.append(day[:len(day) - 2])

        return '-'.join(ans)
