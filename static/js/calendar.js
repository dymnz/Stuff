var currentTime = new Date();
var year = currentTime.getFullYear();
var month = currentTime.getMonth() + 1;
var date = currentTime.getDate();

var prev = document.getElementById("prev");
prev.onclick = function() {
  if (month == 1) {
    month = 12;
    year--;
  } else {
    month--;
  }
  update_calendar();
}

var next = document.getElementById("next");
next.onclick = function() {
  if (month == 12) {
    month = 1;
    year++;
  } else {
    month++;
  }
  update_calendar();
}

var today = document.getElementById("today");
today.href = window.location.href + 'date?date=' + year + '_' + month + '_' + date;

var storage = document.getElementById("storage");
storage.href = window.location.href + 'storage'

var cost = document.getElementById("cost");
cost.href = window.location.href + 'calendar_cost'


window.onload = function () { 
  update_calendar();
}

function update_calendar() {
  document.getElementById("year").innerHTML = year + "年";
  document.getElementById("month").innerHTML = month + " 月";

  var list = document.getElementById("days_list");
  list.innerHTML = "";

  for (var i = 0 ; i < daysInMonth(month, year) ; i++) {
    var entry = document.createElement('a');
    entry.appendChild(document.createTextNode(i+1));
    entry.href = window.location.href + 'date?date=' + year + '_' + month + '_' + (i+1);

    if (year == currentTime.getFullYear() && month == currentTime.getMonth() + 1 && date == (i+1))
      entry.className = "current"

    //entry.href = '{{url_for('show')}}' + '?date=' + (year + '_' + month + '_' + (i+1));
    list.appendChild(entry);
  }

  var month_button = document.getElementById("this_month");
  month_button.href = window.location.href + 'month?month=' + year + '_' + month;

}

function daysInMonth(month, year) {
  return new Date(year, month, 0).getDate();
}