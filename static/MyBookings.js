// let rd=document.getElementById("text1")
// const CanBook=document.getElementById('CanBook')
const tbody = document.querySelector('tbody')
const trip = document.getElementById('inptrip')
const DateT = document.getElementById('inpDate')
const Time = document.getElementById('InpTime')
const purpose = document.getElementById('inpPurpose')
const Seats = document.getElementById('inpSeats')
const Day = document.getElementById('inpDay')
// const id=document.getElementById('Sno')
const Submit = document.getElementById('Submit')
const table = document.querySelector('table');
const form=document.getElementById("Formsub")

console.log(r)
// document.getElementById('text1').innerText=r.data["Monday"][0].trip;
document.getElementById('Name').innerText = r.name_user;
// document.getElementById('CanBook').innerText=r.Messagex;
// console.log(CanBook);
// console.log(text)
console.log(r.data)
k = 1
// id=[]
// Time=[]
// date=[]
// Trip=[]
// Seats=[]
// document.getElementById('Name').innerText=r.name_user;
for (y in r.data) {
    console.log(y)
    let x = r.data[y];
    console.log(x)
    for (o in x) {
        console.log(typeof k)
        p = x[o]
        // console.log(o)
        console.log(p)
        // id.innerText=k
        trip.value = p.trip
        DateT.value = p.date
        Time.value = p.time
        purpose.value = p.purpose
        Seats.value = p.Seats
        console.log(Seats.value)
        Day.value = p.Day
        tbody.innerHTML += `
            <tr>
                    <td>${k}</td>
                    <td class="trip">${trip.value}</td>
                    <td>${Day.value}</td>
                    <td>${DateT.value}</td>
                    <td>${Time.value}</td>
                    <td>${purpose.value}</td>
                    <td>${Seats.value}</td>
                    <td><button class="Cancel">Cancel</button></td>        
            </tr>
        `

        k += 1
        console.log(k)
    }
}
table.addEventListener('click', (e) => {
    if (!e.target.classList.contains('Cancel')) {
        return;
    }
    if (confirm("Cancel my Booking")){
        console.log(trip.value);
        console.log(Day.value);
        console.log("CancelBooking")
        const btn = e.target;
        var a = btn.closest('tr').cells[1].innerText
        var b = btn.closest('tr').cells[2].innerText
        var c = btn.closest('tr').cells[3].innerText
        var d = btn.closest('tr').cells[4].innerText
        var e = btn.closest('tr').cells[5].innerText
        var f = btn.closest('tr').cells[6].innerText
        DateT.value = c
        Time.value = d;
        purpose.value = e;
        Seats.value = f;
        Day.value = b;
        trip.value = a;
        console.log(Seats.value);
        // console.log(a[2])
        console.log("Clicked");
        form.submit();
        // location.reload()
    }
    
    // document.getElementById("Submit").trigger("click");
});

// console.log(Seats)
// rd.innerText=i