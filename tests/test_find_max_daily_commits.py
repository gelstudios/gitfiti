from gitfiti import find_max_daily_commits, parse_contributions_calendar


CONTRIBUTIONS_CALENDAR_SVG = '''\
<svg width="721" height="110" class="js-calendar-graph-svg">
  <g transform="translate(20, 20)">
      <g transform="translate(624, 0)">
          <rect class="day" width="11" height="11" y="0" fill="#eeeeee" data-count="0" data-date="2016-05-08"/>
          <rect class="day" width="11" height="11" y="13" fill="#eeeeee" data-count="0" data-date="2016-05-09"/>
          <rect class="day" width="11" height="11" y="26" fill="#eeeeee" data-count="0" data-date="2016-05-10"/>
          <rect class="day" width="11" height="11" y="39" fill="#eeeeee" data-count="0" data-date="2016-05-11"/>
          <rect class="day" width="11" height="11" y="52" fill="#d6e685" data-count="6" data-date="2016-05-12"/>
          <rect class="day" width="11" height="11" y="65" fill="#eeeeee" data-count="0" data-date="2016-05-13"/>
          <rect class="day" width="11" height="11" y="78" fill="#eeeeee" data-count="0" data-date="2016-05-14"/>
      </g>
      <g transform="translate(637, 0)">
          <rect class="day" width="11" height="11" y="0" fill="#eeeeee" data-count="0" data-date="2016-05-15"/>
          <rect class="day" width="11" height="11" y="13" fill="#eeeeee" data-count="0" data-date="2016-05-16"/>
          <rect class="day" width="11" height="11" y="26" fill="#eeeeee" data-count="0" data-date="2016-05-17"/>
          <rect class="day" width="11" height="11" y="39" fill="#eeeeee" data-count="0" data-date="2016-05-18"/>
          <rect class="day" width="11" height="11" y="52" fill="#eeeeee" data-count="0" data-date="2016-05-19"/>
          <rect class="day" width="11" height="11" y="65" fill="#eeeeee" data-count="0" data-date="2016-05-20"/>
          <rect class="day" width="11" height="11" y="78" fill="#d6e685" data-count="6" data-date="2016-05-21"/>
      </g>
      <g transform="translate(650, 0)">
          <rect class="day" width="11" height="11" y="0" fill="#1e6823" data-count="84" data-date="2016-05-22"/>
          <rect class="day" width="11" height="11" y="13" fill="#d6e685" data-count="16" data-date="2016-05-23"/>
          <rect class="day" width="11" height="11" y="26" fill="#d6e685" data-count="4" data-date="2016-05-24"/>
          <rect class="day" width="11" height="11" y="39" fill="#d6e685" data-count="8" data-date="2016-05-25"/>
          <rect class="day" width="11" height="11" y="52" fill="#eeeeee" data-count="0" data-date="2016-05-26"/>
          <rect class="day" width="11" height="11" y="65" fill="#eeeeee" data-count="0" data-date="2016-05-27"/>
          <rect class="day" width="11" height="11" y="78" fill="#eeeeee" data-count="0" data-date="2016-05-28"/>
      </g>
      <g transform="translate(663, 0)">
          <rect class="day" width="11" height="11" y="0" fill="#eeeeee" data-count="0" data-date="2016-05-29"/>
          <rect class="day" width="11" height="11" y="13" fill="#8cc665" data-count="25" data-date="2016-05-30"/>
          <rect class="day" width="11" height="11" y="26" fill="#1e6823" data-count="66" data-date="2016-05-31"/>
          <rect class="day" width="11" height="11" y="39" fill="#d6e685" data-count="20" data-date="2016-06-01"/>
          <rect class="day" width="11" height="11" y="52" fill="#d6e685" data-count="10" data-date="2016-06-02"/>
          <rect class="day" width="11" height="11" y="65" fill="#eeeeee" data-count="0" data-date="2016-06-03"/>
          <rect class="day" width="11" height="11" y="78" fill="#eeeeee" data-count="0" data-date="2016-06-04"/>
      </g>
      <g transform="translate(676, 0)">
          <rect class="day" width="11" height="11" y="0" fill="#8cc665" data-count="33" data-date="2016-06-05"/>
          <rect class="day" width="11" height="11" y="13" fill="#d6e685" data-count="9" data-date="2016-06-06"/>
          <rect class="day" width="11" height="11" y="26" fill="#eeeeee" data-count="0" data-date="2016-06-07"/>
          <rect class="day" width="11" height="11" y="39" fill="#eeeeee" data-count="0" data-date="2016-06-08"/>
          <rect class="day" width="11" height="11" y="52" fill="#d6e685" data-count="7" data-date="2016-06-09"/>
      </g>
      <text x="0" y="-5" class="month">Jun</text>
      <text x="52" y="-5" class="month">Jul</text>
      <text x="104" y="-5" class="month">Aug</text>
      <text x="169" y="-5" class="month">Sep</text>
      <text x="221" y="-5" class="month">Oct</text>
      <text x="273" y="-5" class="month">Nov</text>
      <text x="338" y="-5" class="month">Dec</text>
      <text x="390" y="-5" class="month">Jan</text>
      <text x="455" y="-5" class="month">Feb</text>
      <text x="507" y="-5" class="month">Mar</text>
      <text x="559" y="-5" class="month">Apr</text>
      <text x="611" y="-5" class="month">May</text>
    <text text-anchor="middle" class="wday" dx="-10" dy="9" style="display: none;">S</text>
    <text text-anchor="middle" class="wday" dx="-10" dy="22">M</text>
    <text text-anchor="middle" class="wday" dx="-10" dy="35" style="display: none;">T</text>
    <text text-anchor="middle" class="wday" dx="-10" dy="48">W</text>
    <text text-anchor="middle" class="wday" dx="-10" dy="61" style="display: none;">T</text>
    <text text-anchor="middle" class="wday" dx="-10" dy="74">F</text>
    <text text-anchor="middle" class="wday" dx="-10" dy="87" style="display: none;">S</text>
  </g>
</svg>
'''


def test_parse_contributions_calendar():
    expected = [
        0, 0, 0, 0, 6, 0, 0,
        0, 0, 0, 0, 0, 0, 6,
        84, 16, 4, 8, 0, 0, 0,
        0, 25, 66, 20, 10, 0, 0,
        33, 9, 0, 0, 7,
    ]

    actual = parse_contributions_calendar(CONTRIBUTIONS_CALENDAR_SVG)

    assert list(actual) == expected


def test_find_max_daily_commits():
    assert find_max_daily_commits(CONTRIBUTIONS_CALENDAR_SVG) == 84
