import unittest
import datetime

class DateTestCases(unittest.TestCase):
  def test_create_date(self):
    """Test for Create date"""
    # Fixture Setup
    # Exercise SUT
    date = datetime.date(2001, 2, 5)
    # Result Verification
    self.assertEqual(2001, date.year)
    self.assertEqual(2, date.month)
    self.assertEqual(5, date.day)
    # Fixture Teardown

  def test_create_invalid_negative_date(self):
    """Test for Invalid negative date"""
    # Fixture Setup
    # Exercise SUT
    with self.assertRaises(ValueError):
      datetime.date(-2024, 3, -4)
    # Result Verification
    # Fixture Teardown

  def test_create_invalid_month_date(self):
    """Test for Create invalid month date"""
    # Fixture Setup
    # Exercise SUT
    with self.assertRaises(ValueError):
      datetime.date(2025, 13, 5)
    # Result Verification
    # Fixture Teardown

  def test_timedelta_addition(self):
    """Test for timedelta addition"""
    # Fixture Setup
    date = datetime.date(2001, 2, 5)
    # Exercise SUT
    new_date = date + datetime.timedelta(5)
    # Result Verification
    self.assertEqual(10, new_date.day)
    # Fixture Teardown

  def test_timedelta_subtraction(self):
    """Test for timedelta subtraction"""
    # Fixture Setup
    date = datetime.date(2001, 2, 5)
    # Exercise SUT
    new_date = date - datetime.timedelta(3)
    # Result Verification
    self.assertEqual(2, new_date.day)
    # Fixture Teardown

  def test_convert_date_to_string(self):
    """Test for convert date to string"""
    # Fixture Setup
    date = datetime.date(2001, 2, 5)
    # Exercise SUT
    date_string = date.strftime("%Y-%m-%d %H:%M:%S")
    # Result Verification
    self.assertIsInstance(date_string, str)
    # Fixture Teardown

  def test_convert_date_format(self):
    """Test for convert date format"""
    # Fixture Setup
    date = datetime.date(2001, 2, 5)
    # Exercise SUT
    date_string = date.strftime("%Y-%m-%d")
    # Result Verification
    self.assertEqual(date_string, "2001-02-05")
    # Fixture Teardown

  def test_convert_date_string_parsing(self):
    """Test for convert date string parsing"""
    # Fixture Setup
    date_string = "2001-02-05"
    # Exercise SUT
    date = datetime.datetime.strptime(date_string, "%Y-%m-%d")
    # Result Verification
    self.assertEqual(date, datetime.datetime(2001, 2, 5))
    # Fixture Teardown

  def test_comparate_two_dates(self):
    """Test for comparate two dates"""
    # Fixture Setup
    date1 = datetime.date(2001, 2, 5)
    date2 = datetime.date(2004, 12, 3)
    # Exercise SUT
    date1_minor_than_date2 = date1 < date2
    # Result Verification
    self.assertTrue(date1_minor_than_date2)
    # Fixture Teardown
  
  def test_timestamp_conversion(self):
    """Test for timestamp conversion"""
    # Fixture Setup
    date = datetime.datetime(2001, 2, 5)
    timestamp = date.timestamp()
    # Exercise SUT
    date_from_timestamp = datetime.datetime.fromtimestamp(timestamp)
    # Result Verification
    self.assertEqual(date_from_timestamp, date)
    # Fixture Teardown

  def test_comparate_equal_dates(self):
    """Test for comparate equal dates"""
    # Fixture Setup
    date1 = datetime.date(2001, 2, 5)
    date2 = datetime.date(2001, 2, 5)
    # Exercise SUT
    are_equal = date1 == date2
    # Result Verification
    self.assertTrue(are_equal)
    # Fixture Teardown

  def test_comparate_greater_date(self):
    """Test for comparate greater date"""
    # Fixture Setup
    date1 = datetime.date(2004, 12, 3)
    date2 = datetime.date(2001, 2, 5)
    # Exercise SUT
    is_greater = date1 > date2
    # Result Verification
    self.assertTrue(is_greater)
    # Fixture Teardown

  def test_timestamp_conversion_with_timezone(self):
    """Test for timestamp conversion with timezone"""
    # Fixture Setup
    date = datetime.datetime(2001, 2, 5, tzinfo=datetime.timezone.utc)
    timestamp = date.timestamp()
    # Exercise SUT
    date_from_timestamp = datetime.datetime.fromtimestamp(timestamp, tz=datetime.timezone.utc)
    # Result Verification
    self.assertEqual(date_from_timestamp, date)
    # Fixture Teardown

  def test_date_difference_negative(self):
    """Test for date difference negative"""
    # Fixture Setup
    date1 = datetime.date(2023, 10, 10)
    date2 = datetime.date(2023, 10, 1)
    # Exercise SUT
    difference = (date2 - date1).days
    # Result Verification
    self.assertEqual(difference, -9)
    # Fixture Teardown

  def test_date_weekday(self):
    """Test for date weekday"""
    # Fixture Setup
    date = datetime.date(2023, 10, 5)
    # Exercise SUT
    weekday = date.weekday()
    # Result Verification
    self.assertEqual(weekday, 3)  # Thursday
    # Fixture Teardown

  def test_date_isoweekday(self):
    """Test for date isoweekday"""
    # Fixture Setup
    date = datetime.date(2023, 10, 5)
    # Exercise SUT
    isoweekday = date.isoweekday()
    # Result Verification
    self.assertEqual(isoweekday, 4)  # Thursday
    # Fixture Teardown

  def test_date_replace(self):
    """Test for date replace"""
    # Fixture Setup
    date = datetime.date(2023, 10, 5)
    # Exercise SUT
    new_date = date.replace(year=2025)
    # Result Verification
    self.assertEqual(new_date, datetime.date(2025, 10, 5))
    # Fixture Teardown

  def test_date_min(self):
    """Test for date min"""
    # Fixture Setup
    # Exercise SUT
    min_date = datetime.date.min
    # Result Verification
    self.assertEqual(min_date, datetime.date(1, 1, 1))
    # Fixture Teardown

  def test_date_max(self):
    """Test for date max"""
    # Fixture Setup
    # Exercise SUT
    max_date = datetime.date.max
    # Result Verification
    self.assertEqual(max_date, datetime.date(9999, 12, 31))
    # Fixture Teardown
  
  def test_date_toordinal(self):
    """Test for date toordinal"""
    # Fixture Setup
    date = datetime.date(2023, 10, 5)
    # Exercise SUT
    ordinal = date.toordinal()
    # Result Verification
    self.assertEqual(ordinal, 738798) 
    # Fixture Teardown
  
  def test_date_fromordinal(self):
    """Test for date fromordinal"""
    # Fixture Setup
    ordinal = 738798
    # Exercise SUT
    date = datetime.date.fromordinal(ordinal)
    # Result Verification
    self.assertEqual(date, datetime.date(2023, 10, 5))
    # Fixture Teardown
  
  def test_date_fromisoformat(self):
    """Test for date fromisoformat"""
    # Fixture Setup
    iso_date = "2023-10-05"
    # Exercise SUT
    date = datetime.date.fromisoformat(iso_date)
    # Result Verification
    self.assertEqual(date, datetime.date(2023, 10, 5))
    # Fixture Teardown
  
  def test_date_isoformat(self):
    """Test for date isoformat"""
    # Fixture Setup
    date = datetime.date(2023, 10, 5)
    # Exercise SUT
    iso_format = date.isoformat()
    # Result Verification
    self.assertEqual(iso_format, "2023-10-05")
    # Fixture Teardown
  
  def test_date_timetuple(self):
    """Test for date timetuple"""
    # Fixture Setup
    date = datetime.date(2023, 10, 5)
    # Exercise SUT
    timetuple = date.timetuple()
    # Result Verification
    self.assertEqual(timetuple.tm_year, 2023)
    self.assertEqual(timetuple.tm_mon, 10)
    self.assertEqual(timetuple.tm_mday, 5)
    # Fixture Teardown
  
  def test_date_isocalendar(self):
    """Test for date isocalendar"""
    # Fixture Setup
    date = datetime.date(2023, 10, 5)
    # Exercise SUT
    isocalendar = date.isocalendar()
    # Result Verification
    self.assertEqual(isocalendar.year, 2023)
    self.assertEqual(isocalendar.week, 40)
    self.assertEqual(isocalendar.weekday, 4)
    # Fixture Teardown

  def test_date_replace_multiple_fields(self):
    """Test for date replace multiple fields"""
    # Fixture Setup
    date = datetime.date(2023, 10, 5)
    # Exercise SUT
    new_date = date.replace(year=2025, month=12, day=25)
    # Result Verification
    self.assertEqual(new_date, datetime.date(2025, 12, 25))
    # Fixture Teardown
  
if __name__ == "__main__":
  unittest.main(verbosity=2)