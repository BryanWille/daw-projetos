function calculateTime(){
    let date = new Date();
    
    var weekDay = date.getDay();
    var day = date.getDate();
    var month = date.getMonth();
    var year = date.getFullYear();
    var hours = date.getHours();
    var minutes = date.getMinutes();
    var seconds = date.getSeconds();

    var dayNames = ["DOM", "SEG", "TER", "QUA", "QUI", "SEX", "SAB"];
    var monthNames = ["JAN", "FEV", "MAR", "ABR", "MAI", "JUN", "JUL", "AGO", "SET", "OUT", "NOV", "DEZ"];

    hours = hours < 10 ? "0" + hours : hours;
    minutes = minutes < 10 ? "0" + minutes : minutes;
    seconds = seconds < 10 ? "0" + seconds : seconds;

    var fullDate = day + "/" + monthNames[month] +"/" +year;

    let h = document.getElementById("hours");
    let m = document.getElementById("minutes");
    let s = document.getElementById("seconds");
    let w = document.getElementById("week-day")
    let c = document.getElementById("current-date")

    h.innerHTML = hours;
    m.innerHTML = minutes;
    s.innerHTML = seconds;

    w.innerHTML = dayNames[weekDay];
    c.innerHTML = fullDate;

    setTimeout(calculateTime, 200);
    
    var r = document.querySelector(":root");
    if (hours < 18){
        r.style.setProperty("--bgcolor", "#4DAFE0");
        r.style.setProperty("--contrast-color", "#FFAB10");
        r.style.setProperty("--lighter-color", "#FFFFFF");
        r.style.setProperty("--dark-color", "#2C2C2C;")
    } else {
        r.style.setProperty("--bgcolor", "#091921");
        r.style.setProperty("--contrast-color", "#FF105E");
        r.style.setProperty("--lighter-color", "##999A9A");
        r.style.setProperty("--dark-color", "#2C2C2C;")
    }
}

window.addEventListener("load", calculateTime);
