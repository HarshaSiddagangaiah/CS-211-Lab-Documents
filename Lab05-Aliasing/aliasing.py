""" ASUO schedule clubs for students."""

from typing import List, Set, Dict, Optional


class Student(object):

    def __init__(self, name: str, interests: List[str]):
        self.name = name
        self.interests = interests
        self.freetimes = set([8, 9, 10, 11, 12, 13, 14, 15])
        self.meetings: List[int] = []

    def schedule_meeting(self, time: int):
        if time in self.freetimes:
            self.freetimes.remove(time)
            self.meetings.append(time)


class Club:

    def __init__(self, name: str):
        self.name = name
        self.members: List[Student] = []
        self.meeting_time: Optional[int] = None

    def join(self, student: Student):
        return self.members.append(student)

    def find_common_time(self) -> int:
        for time in range(8, 16):
            common_time = True
            for student in self.members:
                if time not in student.freetimes:
                    common_time = False
            if common_time is True:
                return time
        return 0

    def schedule(self, time: int):
        for student in self.members:
            student.schedule_meeting(time)
        self.meeting_time = time

    def __str__(self) -> str:
        member_names = [member.name for member in self.members]
        return f"{self.name} ({', '.join(member_names)})"


class ASUO:

    def __init__(self):
        self.students: List[Student] = []
        self.clubs: List[Club] = []

    def enroll(self, s: Student):
        self.students.append(s)

    def form_clubs(self):
        clubs_to_form: Dict[str, Club] = {}
        for students in self.students:
            for interest in students.interests:
                if interest not in clubs_to_form:
                    clubs_to_form[interest] = Club(interest)
                clubs_to_form[interest].join(students)
            self.clubs = clubs_to_form.values()

    def schedule_clubs(self):
        for club in self.clubs:
            time = club.find_common_time()
            if time != 0:
                club.schedule(time)

    def print_club_schedule(self):
        for club in self.clubs:
            if club.meeting_time is not None:
                print(f"{club} meets at {club.meeting_time}")


if __name__ == "__main__":
    asuo = ASUO()
    asuo.enroll(Student("Marty", ["badminton", "robotics"]))
    asuo.enroll(Student("Kim", ["backgammon"]))
    asuo.enroll(Student("Tara", ["robotics", "horticulture", "chess"]))
    asuo.enroll(Student("George", ["chess", "badminton"]))

    asuo.form_clubs()
    asuo.schedule_clubs()
    asuo.print_club_schedule()
