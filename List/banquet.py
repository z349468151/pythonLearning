attendees = []


def send_invite(attendees):
    for attendee in attendees:
        print(attendee.capitalize() + ' well come to the banquet.')


def popAttendee(attendees, index):
    pop = attendees.pop(index)
    print(pop.capitalize() + ', I am sorry that can not have a dinner with you.')


attendees.append('jack')
attendees.append('zhoulong')
attendees.append('xiaowo')
print('I will invited' + str(attendees) + 'to the banquet.')
cannot_attend = attendees.pop(attendees.index('zhoulong'))
print('But ' + cannot_attend + ' can not attend the banquet.')
attendees.append('zl')
attendees.insert(0, 'lukaicheng')
attendees.insert(0, 'maoyeye')
attendees.append('tuanzi')
send_invite(attendees)
print('Due to the table can not arrive , its only can invite two customers to the banquet.')
for i in range(0, len(attendees) - 2):
    popAttendee(attendees, 0)
send_invite(attendees)
for i in range(0, len(attendees)):
    del attendees[0]
print(attendees)
