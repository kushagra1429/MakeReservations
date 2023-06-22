// let rd=document.getElementById("text1")
// const CanBook=document.getElementById('CanBook')
const tbody = document.querySelector('tbody')
const trip = document.getElementById('inptrip')
const DateT = document.getElementById('inpDate')
const Time = document.getElementById('InpTime')
const purpose = document.getElementById('inpPurpose')
const Seats = document.getElementById('inpSeats')
const mobile=document.getElementById("Mobile")
const Day = document.getElementById('inpDay')
// const id=document.getElementById('Sno')
const CodeId=document.getElementById('CodeId')
const Submit = document.getElementById('Submit')
const table = document.querySelector('table');
const form=document.getElementById("Formsub")
const Nameee=document.getElementById('Nameee')
const TripSelect = document.getElementById('Trip');
const day=document.getElementById('Day');
const time=document.getElementById('time');
console.log(r)
// document.getElementById('text1').innerText=r.data["Monday"][0].trip;
document.getElementById('Name').innerText = r.name_user;
// document.getElementById('CanBook').innerText=r.Messagex;
// console.log(CanBook);
// console.log(text)
console.log(r.data)
k = 1
ag=1
bn=1
po = 1
tyui=1
tyu=1
yui=1
uiop=1
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
        console.log(p.Code)


        // id.innerText=k
        Nameee.value=p.Name
        mobile.value=p.MobileNumber
        console.log(Nameee.value)
        trip.value = p.trip
        CodeId.value=p.Code
        console.log(CodeId.value)
        DateT.value = p.date
        Time.value = p.time
        purpose.value = p.purpose
        Seats.value = p.Seats
        console.log(Seats.value)
        Day.value = p.Day
        tbody.innerHTML += `
            <tr>
                    <td>${k}</td>
                    <td>${Nameee.value}</td>
                    <td>${CodeId.value}</td>
                    <td>${mobile.value}</td>
                    <td>${trip.value}</td>
                    <td>${Day.value}</td>
                    <td>${DateT.value}</td>
                    <td>${Time.value}</td>
                    <td>${purpose.value}</td>
                    <td>${Seats.value}</td>

                    
      
            </tr>
        `

        k += 1
        console.log(k)
        rtyui=table.rows.length
        console.log(rtyui)
    }
}
// day.addEventListener('click', ()=>{
//     console.log('True')
//     // table.deleteRow(6)
//     for (f=1; f<rtyui+1; f++){
//         table.deleteRow(f)
//         // console.log('gwcfvnakjh ')

//     }
// })
// day.addEventListener('change', ()=>{
    
//     console.log("Print")
//     if (day.value=="Monday"){
//         for (y in r.data) {
//             // console.log(y)
//             let x = r.data[y];
//             console.log(x)
        
//         for (o in x) {
//             // console.log(typeof k)
//             p = x[o]
//             // console.log(o)
//             // console.log(p)
//             // console.log(p.Code)
//             switch (p.Day) {
//                 case "Monday":
//                     Nameee.value=p.Name
//                     // console.log(Nameee.value)
//                     trip.value = p.trip
//                     // console.log(trip.value)
//                     CodeId.value=p.Code
//                     // console.log(CodeId.value)
//                     DateT.value = p.date
//                     // console.log(DateT.value)
//                     Time.value = p.time
//                     // console.log(Time.value)
//                     purpose.value = p.purpose
//                     Seats.value = p.Seats
//                     // console.log(Seats.value)
//                     Day.value = p.Day
//                     tbody.innerHTML += `
//                         <tr>
//                                 <td>${ag}</td>
//                                 <td>${Nameee.value}</td>
//                                 <td>${CodeId.value}</td>
//                                 <td>${trip.value}</td>
//                                 <td>${Day.value}</td>
//                                 <td>${DateT.value}</td>
//                                 <td>${Time.value}</td>
//                                 <td>${purpose.value}</td>
//                                 <td>${Seats.value}</td>
//                         </tr>
//                     `
//                     ag += 1
//                     console.log(ag)
                    
//                     break;
         
//                 default:
//                     break;
//             }
//     }
//     }
//     }
//     if (day.value=="Tuesday"){
//         for (y in r.data) {
//             // console.log(y)
//             let x = r.data[y];
//             console.log(x)
        
//         for (o in x) {
//             // console.log(typeof k)
//             p = x[o]
//             // console.log(o)
//             // console.log(p)
//             // console.log(p.Code)
//             switch (p.Day) {
//                 case "Tuesday":
//                     Nameee.value=p.Name
//                     console.log(Nameee.value)
//                     trip.value = p.trip
//                     console.log(trip.value)
//                     CodeId.value=p.Code
//                     console.log(CodeId.value)
//                     DateT.value = p.date
//                     console.log(DateT.value)
//                     Time.value = p.time
//                     console.log(Time.value)
//                     purpose.value = p.purpose
//                     Seats.value = p.Seats
//                     console.log(Seats.value)
//                     Day.value = p.Day
//                     tbody.innerHTML += `
//                         <tr>
//                                 <td>${bn}</td>
//                                 <td>${Nameee.value}</td>
//                                 <td>${CodeId.value}</td>
//                                 <td>${trip.value}</td>
//                                 <td>${Day.value}</td>
//                                 <td>${DateT.value}</td>
//                                 <td>${Time.value}</td>
//                                 <td>${purpose.value}</td>
//                                 <td>${Seats.value}</td>
//                         </tr>
//                     `
//                     bn += 1
//                     console.log(bn)
//                     rtyui=table.rows.length
//                     console.log(rtyui)
//                     break;

                                        
//                 default:
//                     break;
//             }
//     }
//     }
//     }
//     if (day.value=="Wednessday"){
//         for (y in r.data) {
//             // console.log(y)
//             let x = r.data[y];
//             console.log(x)
        
//         for (o in x) {
//             // console.log(typeof k)
//             p = x[o]
//             // console.log(o)
//             // console.log(p)
//             // console.log(p.Code)
//             switch (p.Day) {

//                 case "Wednessday":
//                     Nameee.value=p.Name
//                     console.log(Nameee.value)
//                     trip.value = p.trip
//                     console.log(trip.value)
//                     CodeId.value=p.Code
//                     console.log(CodeId.value)
//                     DateT.value = p.date
//                     console.log(DateT.value)
//                     Time.value = p.time
//                     console.log(Time.value)
//                     purpose.value = p.purpose
//                     Seats.value = p.Seats
//                     console.log(Seats.value)
//                     Day.value = p.Day
//                     tbody.innerHTML += `
//                         <tr>
//                                 <td>${po}</td>
//                                 <td>${Nameee.value}</td>
//                                 <td>${CodeId.value}</td>
//                                 <td>${trip.value}</td>
//                                 <td>${Day.value}</td>
//                                 <td>${DateT.value}</td>
//                                 <td>${Time.value}</td>
//                                 <td>${purpose.value}</td>
//                                 <td>${Seats.value}</td>
//                         </tr>
//                     `
//                     po += 1
//                     console.log(po)
                    
//                     break;
                                        
//                 default:
//                     break;
//             }
//     }
//     }
//     }
//     if (day.value=="Thursday"){
//         for (y in r.data) {
//             // console.log(y)
//             let x = r.data[y];
//             console.log(x)
        
//         for (o in x) {
//             // console.log(typeof k)
//             p = x[o]
//             // console.log(o)
//             // console.log(p)
//             // console.log(p.Code)
//             switch (p.Day) {
//                 case "Thursday":
//                     Nameee.value=p.Name
//                     console.log(Nameee.value)
//                     trip.value = p.trip
//                     console.log(trip.value)
//                     CodeId.value=p.Code
//                     console.log(CodeId.value)
//                     DateT.value = p.date
//                     console.log(DateT.value)
//                     Time.value = p.time
//                     console.log(Time.value)
//                     purpose.value = p.purpose
//                     Seats.value = p.Seats
//                     console.log(Seats.value)
//                     Day.value = p.Day
//                     tbody.innerHTML += `
//                         <tr>
//                                 <td>${tyui}</td>
//                                 <td>${Nameee.value}</td>
//                                 <td>${CodeId.value}</td>
//                                 <td>${trip.value}</td>
//                                 <td>${Day.value}</td>
//                                 <td>${DateT.value}</td>
//                                 <td>${Time.value}</td>
//                                 <td>${purpose.value}</td>
//                                 <td>${Seats.value}</td>
//                         </tr>
//                     `
//                     tyui += 1
//                     console.log(tyui)
//                     break;
                   
//                 default:
//                     break;
//             }
//     }
//     }
//     }
//     if (day.value=="Friday"){
//         for (y in r.data) {
//             // console.log(y)
//             let x = r.data[y];
//             console.log(x)
        
//         for (o in x) {
//             // console.log(typeof k)
//             p = x[o]
//             // console.log(o)
//             // console.log(p)
//             // console.log(p.Code)
//             switch (p.Day) {
//                 case "Friday":
//                     Nameee.value=p.Name
//                     console.log(Nameee.value)
//                     trip.value = p.trip
//                     console.log(trip.value)
//                     CodeId.value=p.Code
//                     console.log(CodeId.value)
//                     DateT.value = p.date
//                     console.log(DateT.value)
//                     Time.value = p.time
//                     console.log(Time.value)
//                     purpose.value = p.purpose
//                     Seats.value = p.Seats
//                     console.log(Seats.value)
//                     Day.value = p.Day
//                     tbody.innerHTML += `
//                         <tr>
//                                 <td>${tyu}</td>
//                                 <td>${Nameee.value}</td>
//                                 <td>${CodeId.value}</td>
//                                 <td>${trip.value}</td>
//                                 <td>${Day.value}</td>
//                                 <td>${DateT.value}</td>
//                                 <td>${Time.value}</td>
//                                 <td>${purpose.value}</td>
//                                 <td>${Seats.value}</td>
//                         </tr>
//                     `
//                     tyu += 1
//                     console.log(tyu)
//                     break;
                

                
                                        
//                 default:
//                     break;
//             }
//     }
//     }
//     }
//     if (day.value=="Saturday"){
//         for (y in r.data) {
//             // console.log(y)
//             let x = r.data[y];
//             console.log(x)
        
//         for (o in x) {
//             // console.log(typeof k)
//             p = x[o]
//             // console.log(o)
//             // console.log(p)
//             // console.log(p.Code)
//             switch (p.Day) {
//                 case "Saturday":
//                     Nameee.value=p.Name
//                     console.log(Nameee.value)
//                     trip.value = p.trip
//                     console.log(trip.value)
//                     CodeId.value=p.Code
//                     console.log(CodeId.value)
//                     DateT.value = p.date
//                     console.log(DateT.value)
//                     Time.value = p.time
//                     console.log(Time.value)
//                     purpose.value = p.purpose
//                     Seats.value = p.Seats
//                     console.log(Seats.value)
//                     Day.value = p.Day
//                     tbody.innerHTML += `
//                         <tr>
//                                 <td>${yui}</td>
//                                 <td>${Nameee.value}</td>
//                                 <td>${CodeId.value}</td>
//                                 <td>${trip.value}</td>
//                                 <td>${Day.value}</td>
//                                 <td>${DateT.value}</td>
//                                 <td>${Time.value}</td>
//                                 <td>${purpose.value}</td>
//                                 <td>${Seats.value}</td>
//                         </tr>
//                     `
//                     yui += 1
//                     console.log(yui)
                    
//                     break;

                       
//                 default:
//                     break;
//             }
//     }
//     }
//     }
//     if (day.value=="Sunday"){
//         for (y in r.data) {
//             // console.log(y)
//             let x = r.data[y];
//             console.log(x)
        
//         for (o in x) {
//             // console.log(typeof k)
//             p = x[o]
//             // console.log(o)
//             // console.log(p)
//             // console.log(p.Code)
//             switch (p.Day) {
//                 case "Sunday":
//                     Nameee.value=p.Name
//                     console.log(Nameee.value)
//                     trip.value = p.trip
//                     console.log(trip.value)
//                     CodeId.value=p.Code
//                     console.log(CodeId.value)
//                     DateT.value = p.date
//                     console.log(DateT.value)
//                     Time.value = p.time
//                     console.log(Time.value)
//                     purpose.value = p.purpose
//                     Seats.value = p.Seats
//                     console.log(Seats.value)
//                     Day.value = p.Day
//                     tbody.innerHTML += `
//                         <tr>
//                                 <td>${uiop}</td>
//                                 <td>${Nameee.value}</td>
//                                 <td>${CodeId.value}</td>
//                                 <td>${trip.value}</td>
//                                 <td>${Day.value}</td>
//                                 <td>${DateT.value}</td>
//                                 <td>${Time.value}</td>
//                                 <td>${purpose.value}</td>
//                                 <td>${Seats.value}</td>
//                         </tr>
//                     `
//                     uiop+= 1
//                     console.log(uiop)
//                     break;
                                        
//                 default:
//                     break;
//             }
//     }
//     }
//     }
        
        
// }
// )




