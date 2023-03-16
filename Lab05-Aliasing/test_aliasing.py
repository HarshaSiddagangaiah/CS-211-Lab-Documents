import unittest
from aliasing import Student, Club, ASUO


class TestASUO(unittest.TestCase):

    def test_enroll(self):
        asuo = ASUO()
        s1 = Student("Marty", ["badminton", "robotics"])
        asuo.enroll(s1)
        self.assertEqual(asuo.students, [s1])

    def test_form_clubs(self):
        asuo = ASUO()
        s1 = Student("Marty", ["badminton", "robotics"])
        s2 = Student("Kim", ["backgammon"])
        asuo.enroll(s1)
        asuo.enroll(s2)
        asuo.form_clubs()
        expected_clubs = [Club("badminton"), Club("robotics"), Club("backgammon")]
        for club in expected_clubs:
            self.assertIn(club, asuo.clubs)

    def test_schedule_clubs(self):
        asuo = ASUO()
        s1 = Student("Marty", ["badminton", "robotics"])
        s2 = Student("Kim", ["backgammon"])
        asuo.enroll(s1)
        asuo.enroll(s2)
        asuo.form_clubs()
        asuo.schedule_clubs()
        for club in asuo.clubs:
            self.assertIsNotNone(club.meeting_time)

    def test_print_club_schedule(self):
        asuo = ASUO()
        s1 = Student("Marty", ["badminton", "robotics"])
        s2 = Student("Kim", ["backgammon"])
        asuo.enroll(s1)
        asuo.enroll(s2)
        asuo.form_clubs()
        asuo.schedule_clubs()
        expected_output = "badminton (Marty, George) meets at 11\nrobotics (Marty, Tara) meets at 13\nbackgammon (Kim) meets at 8\n"
        with captured_output() as (out, err):
            asuo.print_club_schedule()
        self.assertEqual(out, expected_output)


if __name__ == '__main__':
    unittest.main()
