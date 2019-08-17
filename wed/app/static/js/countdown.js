$(document).ready(function() {

// Set the date we're counting down to
    function newNum(numid){
        var num = document.createElement("span")
        $(num).attr("id",numid)
        $(num).addClass("huge")
        return num
    }
    function up(numid, val)
    {
        $("#"+numid).html(val)
    }
    var countDownDate = new Date("Sep 14, 2019 17:18:00").getTime();
    var countdown = document.createElement("div")
    // $(countdown).append("开始还有:<br>")
    $(countdown).append(newNum("daytag"))
    $(countdown).append("天")
    $(countdown).append(newNum("hourtag"))
    $(countdown).append("小时")
    $(countdown).append(newNum("minutetag"))
    $(countdown).append("分")
    $(countdown).append(newNum("secondtag"))
    $(countdown).append("秒")
    $("#countdown").html(countdown)

// Update the count down every 1 second
    var x = setInterval(function () {

        // Get today's date and time
        var now = new Date().getTime();

        // Find the distance between now and the count down date
        var distance = countDownDate - now;

        // Time calculations for days, hours, minutes and seconds
        var days = Math.floor(distance / (1000 * 60 * 60 * 24));
        var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        var seconds = Math.floor((distance % (1000 * 60)) / 1000);

        // update the time elements
        up("daytag",days);
        up("hourtag", hours);
        up("minutetag", minutes);
        up("secondtag",seconds);


        // If the count down is over, write some text
        if (distance < 0) {
            clearInterval(x);
            document.getElementById("countdown").innerHTML = "结婚啦!";
        }
    }, 1000);

})