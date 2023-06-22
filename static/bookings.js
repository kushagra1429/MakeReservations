const container = document.querySelector('.bus');
const seats = document.querySelectorAll('.rowX .seat:not(.occupied');
const count = document.getElementById('count');
const total = document.getElementById('total');
const TripSelect = document.getElementById('Trip');
const day=document.getElementById('Day');
const time=document.getElementById('time');
const bookedSeats=document.getElementById("BookedSeats");
const NumberOfSeats=document.getElementById("NumberOfSeats");
const Name=document.getElementById('EmployeeName');
const Mobile=document.getElementById('EmployeeMobile');
const Code=document.getElementById('Code');
const Sb=document.querySelector('.Submit');
const SEATS=document.getElementsByClassName('seat');
const Datee=document.getElementById('Date')
const ErrorDay= document.getElementById('alertDay')

Name.value=r.data.name;
Mobile.value=r.data.Mobile;
Code.value=r.data.Code;
y=r.day["BookedSeats1"];
// console.log(y)
console.log(r.day)
for (i in r.day){
  var mu=r.day[i]
  for (c in mu){
    console.log(mu[c])
  }
}

let ticketTrip = TripSelect.value;
let SelectedDay=day.value;
// let NumberOfSeats.value=selectedSeatsCount;

Datee.addEventListener('change', ()=>{
  for(x=3; x<SEATS.length; x++){
    // console.log(SEATS[x].id)
    // console.log("Print")
    SEATS[x].className="seat"
  }
  // setTimeout(() => {
    
  // }, 1000);
  
})

day.addEventListener('change', (e) => {
  SelectedDay = e.target.value;
  console.log(SelectedDay)
  if (SelectedDay!=="Select"){
    TripSelect.disabled=false;
  }
  console.log(SelectedDay);
  SetTrip(SelectedDay, TripSelect);
  // console.log(TripSelect.value)
  // updateSelectedCount();
});

function SetTrip(SelectedDay, trip){
  trip.innerHTML="";
  switch (SelectedDay) {
    case "Monday":
      var TripOptions=["Select|Select", "Township to Kota Station|Township to Kota Station"];
      break;
    case "Tuesday":
      var TripOptions=["Select|Select", "Kota Station to Township|Kota Station to Township","Township to Kota Station|Township to Kota Station"];
      break;
    case "Wednessday":
      var TripOptions=["Select|Select", "Township to Kota Station|Township to Kota Station", "Kota Station to Township|Kota Station to Township"];
      break;
    case "Thursday":
      var TripOptions=["Select|Select", "Township to Kota Station|Township to Kota Station", "Township to Baran|Township to Baran", "Baran to Township|Baran to Township"];
      break;
    case "Friday":
      var TripOptions=["Select|Select", "Kota Station to Township|Kota Station to Township","Township to Kota Station|Township to Kota Station"];
      break;
    case "Saturday":
      var TripOptions=["Select|Select", "Kota Station to Township|Kota Station to Township","Township to Kota Station|Township to Kota Station"];
      break;
    case "Sunday":
      var TripOptions=["Select|Select", "Township to Kota Station|Township to Kota Station", "Kota Station to Township|Kota Station to Township"];
      break;
    default:
      break;
  }
  for (var options in TripOptions){
    var pair=TripOptions[options].split("|");
    // console.log(pair)
    var newOption=document.createElement('option');
    newOption.value=pair[0];
    newOption.innerHTML=pair[1];
    trip.options.add(newOption);
  }
}
// Trip select event
TripSelect.addEventListener('change', (e) => {
  ticketTrip = e.target.value;
  if (ticketTrip!=="Select"){
    time.disabled=false;
  }
  console.log(SelectedDay);
  setTripTime(SelectedDay, ticketTrip, time);
  // updateSelectedCount();
  // switch (SelectedDay) {
  //   case "Monday": 
  //     if (ticketTrip=="Township to Kota Station"){
  //       console.log("True")
  //       var y=r.day["BookedSeats1"]
  //       console.log(y)
  //       u=[]
  //       for (var x in y){
  //         console.log(y[x])
  //         console.log(typeof y[x])
  //         var q=y[x].split(',')
  //         console.log(q)
  //         for (var e in q){
  //           t=q[e]
  //           if (t!=""){
  //             var xl=document.getElementById(t).id;
  //             document.getElementById(xl).classList.toggle('occupied');
  //             u.push(xl)
  //           }
  //         }
  //       }
  //     }     
  //     break;
  //   case "Tuesday":
  //     if(ticketTrip=="Township to Kota Station"){
  //       var y=r.day["BookedSeats2"]
  //         for (var x in y){
  //           console.log(y[x])
  //           console.log(typeof y[x])
  //           var q=y[x].split(',')
  //           console.log(q)
  //           for (var e in q){
  //             // console.log(q[e])
  //             // console.log(typeof e)
  //             t=q[e]
  //             // console.log(t)
  //             if (t!=""){
  //               // console.log("True")
  //               var p=document.getElementById(t).id;
  //               document.getElementById(p).classList.toggle('occupied');
  //               l.push(p)
  //           }
  //         }
  //       }
  //     }     
  //     break;
  //   case "Wednessday":
  //     k=[]
  //     if (ticketTrip=="Township to Kota Station"){
  //       console.log("Wed")
  //       var y=r.day["BookedSeats3A"]
  //       for (var x in y){
  //         console.log(y[x])
  //         console.log(typeof y[x])
  //         var q=y[x].split(',')
  //         console.log(q)
  //         for (var e in q){
  //           // console.log(q[e])
  //           // console.log(typeof e)
  //           t=q[e]
  //           // console.log(t)
  //           if (t!=""){
  //             // console.log("True")
  //             var p=document.getElementById(t).id;
  //             document.getElementById(p).classList.toggle('occupied')
  //             k.push(p)
  //           }
  //         }
  //       }
  //     }
  //     else if(ticketTrip="Kota station to Township"){
  //       var y=r.day["BookedSeats3"]
  //       for (var x in y){
  //         console.log(y[x])
  //         console.log(typeof y[x])
  //         var q=y[x].split(',')
  //         console.log(q)
  //         for (var e in q){
  //           // console.log(q[e])
  //           // console.log(typeof e)
  //           t=q[e]
  //           // console.log(t)
  //           if (t!=""){
  //             // console.log("True")
  //             var p=document.getElementById(t).id;
  //             document.getElementById(p).classList.toggle('occupied')
  //             k.push(p)
  //           }
  //         }
  //       }
  //     }
      
      
  //     break;
  //   case "Thursday":
  //     cl=[]
  //     if (ticketTrip=="Township to Kota Station"){
  //       var y=r.day["BookedSeats4"]
  //       for (var x in y){
  //         console.log(y[x])
  //         console.log(typeof y[x])
  //         var q=y[x].split(',')
  //         console.log(q)
  //         for (var e in q){
  //           // console.log(q[e])
  //           // console.log(typeof e)
  //           t=q[e]
  //           // console.log(t)
  //           if (t!=""){
  //             // console.log("True")
  //             var p=document.getElementById(t).id;
  //             document.getElementById(p).classList.toggle('occupied')
  //             cl.push(p)
  //           }
  //         }
  //       }
  //     }
  //     else if(ticketTrip=="Township to Baran"){
  //       var y=r.day["BookedSeats4A"]
  //       for (var x in y){
  //         console.log(y[x])
  //         console.log(typeof y[x])
  //         var q=y[x].split(',')
  //         console.log(q)
  //         for (var e in q){
  //           // console.log(q[e])
  //           // console.log(typeof e)
  //           t=q[e]
  //           // console.log(t)
  //           if (t!=""){
  //             // console.log("True")
  //             var p=document.getElementById(t).id;
  //             document.getElementById(p).classList.toggle('occupied')
  //             cl.push(p)
  //           }
  //         }
  //       }
  //     }
  //     else if(ticketTrip=="Baran to Township"){
  //       var y=r.day["BookedSeats4B"]
  //       for (var x in y){
  //         console.log(y[x])
  //         console.log(typeof y[x])
  //         var q=y[x].split(',')
  //         console.log(q)
  //         for (var e in q){
  //           // console.log(q[e])
  //           // console.log(typeof e)
  //           t=q[e]
  //           // console.log(t)
  //           if (t!=""){
  //             // console.log("True")
  //             var p=document.getElementById(t).id;
  //             document.getElementById(p).classList.toggle('occupied')
  //             cl.push(p)
  //           }
  //       }
  //     }
  //   }
  //   break;
  //   case "Friday":
  //     if(ticketTrip=="Township to Kota Station"){
  //       var y=r.day["BookedSeats5"]
  //         for (var x in y){
  //           console.log(y[x])
  //           console.log(typeof y[x])
  //           var q=y[x].split(',')
  //           console.log(q)
  //           for (var e in q){
  //             // console.log(q[e])
  //             // console.log(typeof e)
  //             t=q[e]
  //             // console.log(t)
  //             if (t!=""){
  //               // console.log("True")
  //               var p=document.getElementById(t).id;
  //               document.getElementById(p).classList.toggle('occupied');
  //               pl.push(p)
  //           }
  //         }
  //       }
  //     }    
  //     break;
  //   case "Saturday":
  //     ol=[]
  //     if (ticketTrip=="Township to Kota Station"){
  //       var y=r.day["BookedSeats6A"]
  //       console.log(y)
  //       for (var x in y){
  //         console.log(y[x])
  //         console.log(typeof y[x])
  //         var q=y[x].split(',')
  //         console.log(q)
  //         for (var e in q){
  //           // console.log(q[e])
  //           // console.log(typeof e)
  //           t=q[e]
  //           // console.log(t)
  //           if (t!=""){
  //             // console.log("True")
  //             var p=document.getElementById(t).id;
  //             document.getElementById(p).classList.toggle('occupied')
  //             ol.push(p)
  //           }
  //         }
  //       }
  //     }
  //     else if(ticketTrip=="Kota Station to Township"){
  //       var y=r.day["BookedSeats6"]
  //       for (var x in y){
  //         console.log(y[x])
  //         console.log(typeof y[x])
  //         var q=y[x].split(',')
  //         console.log(q)
  //         for (var e in q){
  //           // console.log(q[e])
  //           // console.log(typeof e)
  //           t=q[e]
  //           // console.log(t)
  //           if (t!=""){
  //             // console.log("True")
  //             var p=document.getElementById(t).id;
  //             document.getElementById(p).classList.toggle('occupied')
  //             ol.push(p)
  //           }
  //         }
  //       }
  //     }
  //     break;
  //   case "Sunday":
  //           jl=[]
  //           if (ticketTrip=="Township to Kota Station"){
  //             var y=r.day["BookedSeats7A"]
  //             for (var x in y){
  //               console.log(y[x])
  //               console.log(typeof y[x])
  //               var q=y[x].split(',')
  //               console.log(q)
  //               for (var e in q){
  //                 // console.log(q[e])
  //                 // console.log(typeof e)
  //                 t=q[e]
  //                 // console.log(t)
  //                 if (t!=""){
  //                   // console.log("True")
  //                   var p=document.getElementById(t).id;
  //                   document.getElementById(p).classList.toggle('occupied')
  //                   jl.push(p)
  //                 }
  //               }
  //             }
  //           }
  //           else if (ticketTrip=="Kota Station to Township"){
  //             var y=r.day["BookedSeats7"]
  //             for (var x in y){
  //               console.log(y[x])
  //               console.log(typeof y[x])
  //               var q=y[x].split(',')
  //               console.log(q)
  //               for (var e in q){
  //                 // console.log(q[e])
  //                 // console.log(typeof e)
  //                 t=q[e]
  //                 // console.log(t)
  //                 if (t!=""){
  //                   // console.log("True")
  //                   var p=document.getElementById(t).id;
  //                   document.getElementById(p).classList.toggle('occupied')
  //                   jl.push(p)
  //                 }
  //               }
  //             }
  //           }
            
  //           break;
  //   default:
  //     break;
  // }
});
function setTripTime(SelectedDay, ticketTrip, time){
  time.innerHTML="";
  switch (SelectedDay) {
    case "Monday":
      if (ticketTrip=="Township to Kota Station"){
        var timeOptions=["4:00PM|4:00PM"];
      }
      break;
    case "Tuesday":
      if (ticketTrip=="Kota Station to Township"){
        var timeOptions=["Select|Select", "8:00AM|8:00AM", "8:30PM|8:30PM"];

      }
      else if(ticketTrip=="Township to Kota Station"){
        var timeOptions=["2:00PM|2:00PM"];

      }
      break;

    case "Wednessday":
      if(ticketTrip=="Township to Kota Station"){
        var timeOptions=["7:45PM|7:45PM"];

      }
      else if (ticketTrip=="Kota Station to Township"){
        var timeOptions=["5:30PM|5:30PM"];

      }
      break;

    case "Thursday":
      if(ticketTrip=="Township to Kota Station"){
        var timeOptions=["4:00PM|4:00PM"];
      }
      else if (ticketTrip=="Township to Baran"){
        var timeOptions=["8:30AM|8:30AM"];

      }
      else if ("Baran to township"){
        var timeOptions=["1:00PM|1:00PM"];

      }
      break;

    case "Friday":
      if (ticketTrip=="Kota Station to Township"){
        var timeOptions=["Select|Select", "8:00AM|8:00AM", "8:30PM|8:30PM"];

      }
      else if(ticketTrip=="Township to Kota Station"){
        var timeOptions=["2:00PM|2:00PM"];

      }
      break;

    case "Saturday":
      if(ticketTrip=="Township to Kota Station"){
        var timeOptions=["2:00PM|2:00PM"];

      }
      else if (ticketTrip=="Kota Station to Township"){
        var timeOptions=["8:30PM|8:30PM"];
      }
      break;

    case "Sunday":
      if(ticketTrip=="Township to Kota Station"){
        var timeOptions=["7:45PM|7:45PM"];
      }
      else if (ticketTrip=="Kota Station to Township"){
        var timeOptions=["5:30PM|5:30PM"];
      }
      break;

    default:
      break;
  }
  for (var options in timeOptions){
    var pair=timeOptions[options].split("|");
    // console.log(pair)
    var NewOption=document.createElement('option');
    NewOption.value=pair[0];
    NewOption.innerHTML=pair[1];
    time.options.add(NewOption);
  }

}

time.addEventListener('change',()=>{
  // switch (SelectedDay) {
  //   case "Tuesday":
  //     l=[]
  //     if (ticketTrip=="Kota Station to Township"){
  //       if (time.value=="8:00AM"){
  //         var y=r.day["BookedSeats2A"]
  //         for (var x in y){
  //           console.log(y[x])
  //           console.log(typeof y[x])
  //           var q=y[x].split(',')
  //           console.log(q)
  //           for (var e in q){
  //             t=q[e]
  //             if (t!=""){
  //               var p=document.getElementById(t).id;
  //               document.getElementById(p).classList.toggle('occupied');
  //               l.push(p)
  //             }
  //           }
  //         }
  //       }
  //       else if(time.value=="8:30PM"){
  //         var y=r.day["BookedSeats2B"]
  //         for (var x in y){
  //           console.log(y[x])
  //           console.log(typeof y[x])
  //           var q=y[x].split(',')
  //           console.log(q)
  //           for (var e in q){
  //             // console.log(q[e])
  //             // console.log(typeof e)
  //             t=q[e]
  //             // console.log(t)
  //             if (t!=""){
  //               // console.log("True")
  //               var p=document.getElementById(t).id;
  //               document.getElementById(p).classList.toggle('occupied');
  //               l.push(p)
  //             }
  //           }
  //         }
  //       }
  //     }
  //     break;
      
  //     case "Friday":
  //     pl=[]
  //     if (ticketTrip=="Kota Station to Township"){
  //       if (time.value=="8:00AM"){
  //         var y=r.day["BookedSeats5A"]
  //         for (var x in y){
  //           console.log(y[x])
  //           console.log(typeof y[x])
  //           var q=y[x].split(',')
  //           console.log(q)
  //           for (var e in q){
  //             t=q[e]
  //             if (t!=""){
  //               var p=document.getElementById(t).id;
  //               document.getElementById(p).classList.toggle('occupied');
  //               pl.push(p)
  //           }
  //         }
  //       }
  //       }
  //       else if(time.value=="8:30PM"){
  //         var y=r.day["BookedSeats5B"]
  //         for (var x in y){
  //           console.log(y[x])
  //           console.log(typeof y[x])
  //           var q=y[x].split(',')
  //           console.log(q)
  //           for (var e in q){
  //             // console.log(q[e])
  //             // console.log(typeof e)
  //             t=q[e]
  //             // console.log(t)
  //             if (t!=""){
  //               // console.log("True")
  //               var p=document.getElementById(t).id;
  //               document.getElementById(p).classList.toggle('occupied');
  //               pl.push(p)
  //           }
  //         }
  //       }
  //       }
  //     }
  //     break;
  //   default:
  //     break;
  // }
})

Datee.addEventListener('change', ()=>{
  console.log(Datee.value);
  switch (SelectedDay) {
    case "Monday":
      if (ticketTrip=="Township to Kota Station"){
        var mu=r.day["BookedSeats1"]
        console.log(mu)
        for (c in mu){
          var iop=mu[c].date
          console.log(iop)
          if (iop==Datee.value){
            console.log(mu[c].Seats)
            t=mu[c].Seats
            var q=t.split(',')
            console.log(q)
            console.log(q.length)
            for (y in q){
              console.log(q[y])
              e=q[y]
              if (e!=""){
                var p=document.getElementById(e).id;
                console.log(p);
                document.getElementById(p).classList.toggle('occupied');
              }
            }  
          }
        }
      }
    
      
      break;
    case "Tuesday":
      l=[]
      if (ticketTrip=="Kota Station to Township"){
        if (time.value=="8:00AM"){
          var mu=r.day["BookedSeats2A"]
          console.log(mu)
          for (c in mu){
            var iop=mu[c].date
            console.log(iop)
            if (iop==Datee.value){
              console.log(mu[c].Seats)
              t=mu[c].Seats
              var q=t.split(',')
              console.log(q)
              console.log(q.length)
              for (y in q){
                console.log(q[y])
                e=q[y]
                if (e!=""){
                  var p=document.getElementById(e).id;
                  console.log(p);
                  document.getElementById(p).classList.toggle('occupied');
                }
              }  
            }
          }
        }
        else if(time.value=="8:30PM"){
          var mu=r.day["BookedSeats2B"]
          console.log(mu)
          for (c in mu){
            var iop=mu[c].date
            console.log(iop)
            if (iop==Datee.value){
              console.log(mu[c].Seats)
              t=mu[c].Seats
              var q=t.split(',')
              console.log(q)
              console.log(q.length)
              for (y in q){
                console.log(q[y])
                e=q[y]
                if (e!=""){
                  var p=document.getElementById(e).id;
                  console.log(p);
                  document.getElementById(p).classList.toggle('occupied');
                }
              }  
            }
          }
        }
      }
          else if(ticketTrip=="Township to Kota Station"){
            var mu=r.day["BookedSeats2"]
            console.log(mu)
            for (c in mu){
              var iop=mu[c].date
              console.log(iop)
              if (iop==Datee.value){
                console.log(mu[c].Seats)
                t=mu[c].Seats
                var q=t.split(',')
                console.log(q)
                console.log(q.length)
                for (y in q){
                  console.log(q[y])
                  e=q[y]
                  if (e!=""){
                    var p=document.getElementById(e).id;
                    console.log(p);
                    document.getElementById(p).classList.toggle('occupied');
                  }
                }  
              }
            }
          }     
          break;
    case "Wednessday":
      k=[]
      if (ticketTrip=="Township to Kota Station"){
        console.log("Wed")
        var mu=r.day["BookedSeats3A"]
        console.log(mu)
        for (c in mu){
          var iop=mu[c].date
          console.log(iop)
          if (iop==Datee.value){
            console.log(mu[c].Seats)
            t=mu[c].Seats
            var q=t.split(',')
            console.log(q)
            console.log(q.length)
            for (y in q){
              console.log(q[y])
              e=q[y]
              if (e!=""){
                var p=document.getElementById(e).id;
                console.log(p);
                document.getElementById(p).classList.toggle('occupied');
              }
            }  
          }
        }
      }
      else if(ticketTrip="Kota station to Township"){
        var mu=r.day["BookedSeats3"]
        console.log(mu)
        for (c in mu){
          var iop=mu[c].date
          console.log(iop)
          if (iop==Datee.value){
            console.log(mu[c].Seats)
            t=mu[c].Seats
            var q=t.split(',')
            console.log(q)
            console.log(q.length)
            for (y in q){
              console.log(q[y])
              e=q[y]
              if (e!=""){
                var p=document.getElementById(e).id;
                console.log(p);
                document.getElementById(p).classList.toggle('occupied');
              }
            }  
          }
        }
      }
      break;
    case "Thursday":
      cl=[]
      if (ticketTrip=="Township to Kota Station"){
        var mu=r.day["BookedSeats4"]
        console.log(mu)
        for (c in mu){
          var iop=mu[c].date
          console.log(iop)
          if (iop==Datee.value){
            console.log(mu[c].Seats)
            t=mu[c].Seats
            var q=t.split(',')
            console.log(q)
            console.log(q.length)
            for (y in q){
              console.log(q[y])
              e=q[y]
              if (e!=""){
                var p=document.getElementById(e).id;
                console.log(p);
                document.getElementById(p).classList.toggle('occupied');
              }
            }  
          }
        }
      }
      else if(ticketTrip=="Township to Baran"){
        var mu=r.day["BookedSeats4A"]
        console.log(mu)
        for (c in mu){
          var iop=mu[c].date
          console.log(iop)
          if (iop==Datee.value){
            console.log(mu[c].Seats)
            t=mu[c].Seats
            var q=t.split(',')
            console.log(q)
            console.log(q.length)
            for (y in q){
              console.log(q[y])
              e=q[y]
              if (e!=""){
                var p=document.getElementById(e).id;
                console.log(p);
                document.getElementById(p).classList.toggle('occupied');
              }
            }  
          }
        }
      }
      else if(ticketTrip=="Baran to Township"){
        var mu=r.day["BookedSeats4B"]
        console.log(mu)
        for (c in mu){
          var iop=mu[c].date
          console.log(iop)
          if (iop==Datee.value){
            console.log(mu[c].Seats)
            t=mu[c].Seats
            var q=t.split(',')
            console.log(q)
            console.log(q.length)
            for (y in q){
              console.log(q[y])
              e=q[y]
              if (e!=""){
                var p=document.getElementById(e).id;
                console.log(p);
                document.getElementById(p).classList.toggle('occupied');
              }
            }  
          }
        }
      }
    break;
    case "Friday":
      pl=[]
      if (ticketTrip=="Kota Station to Township"){
        if (time.value=="8:00AM"){
          var mu=r.day["BookedSeats5A"]
          console.log(mu)
          for (c in mu){
            var iop=mu[c].date
            console.log(iop)
            if (iop==Datee.value){
              console.log(mu[c].Seats)
              t=mu[c].Seats
              var q=t.split(',')
              console.log(q)
              console.log(q.length)
              for (y in q){
                console.log(q[y])
                e=q[y]
                if (e!=""){
                  var p=document.getElementById(e).id;
                  console.log(p);
                  document.getElementById(p).classList.toggle('occupied');
                }
              }  
            }
          }
        }
        else if(time.value=="8:30PM"){
          var mu=r.day["BookedSeats5B"]
          console.log(mu)
          for (c in mu){
            var iop=mu[c].date
            console.log(iop)
            if (iop==Datee.value){
              console.log(mu[c].Seats)
              t=mu[c].Seats
              var q=t.split(',')
              console.log(q)
              console.log(q.length)
              for (y in q){
                console.log(q[y])
                e=q[y]
                if (e!=""){
                  var p=document.getElementById(e).id;
                  console.log(p);
                  document.getElementById(p).classList.toggle('occupied');
                }
              }  
            }
          }
        }
      }
      else if(ticketTrip=="Township to Kota Station"){
        var mu=r.day["BookedSeats5"]
        console.log(mu)
        for (c in mu){
          var iop=mu[c].date
          console.log(iop)
          if (iop==Datee.value){
            console.log(mu[c].Seats)
            t=mu[c].Seats
            var q=t.split(',')
            console.log(q)
            console.log(q.length)
            for (y in q){
              console.log(q[y])
              e=q[y]
              if (e!=""){
                var p=document.getElementById(e).id;
                console.log(p);
                document.getElementById(p).classList.toggle('occupied');
              }
            }  
          }
        }
      }    
      break;
    case "Saturday":
      ol=[]
      if (ticketTrip=="Township to Kota Station"){
        var y=r.day["BookedSeats6A"]
        var mu=r.day["BookedSeats6A"]
        console.log(mu)
        for (c in mu){
          var iop=mu[c].date
          console.log(iop)
          if (iop==Datee.value){
            console.log(mu[c].Seats)
            t=mu[c].Seats
            var q=t.split(',')
            console.log(q)
            console.log(q.length)
            for (y in q){
              console.log(q[y])
              e=q[y]
              if (e!=""){
                var p=document.getElementById(e).id;
                console.log(p);
                document.getElementById(p).classList.toggle('occupied');
              }
            }  
          }
        }
      }
      else if(ticketTrip=="Kota Station to Township"){
        var mu=r.day["BookedSeats6"]
        console.log(mu)
        for (c in mu){
          var iop=mu[c].date
          console.log(iop)
          if (iop==Datee.value){
            console.log(mu[c].Seats)
            t=mu[c].Seats
            var q=t.split(',')
            console.log(q)
            console.log(q.length)
            for (y in q){
              console.log(q[y])
              e=q[y]
              if (e!=""){
                var p=document.getElementById(e).id;
                console.log(p);
                document.getElementById(p).classList.toggle('occupied');
              }
            }  
          }
        }
      }
      break;
    case "Sunday":
                jl=[]
                if (ticketTrip=="Township to Kota Station"){
                  var mu=r.day["BookedSeats7A"]
                  console.log(mu)
                  for (c in mu){
                    var iop=mu[c].date
                    console.log(iop)
                    if (iop==Datee.value){
                      console.log(mu[c].Seats)
                      t=mu[c].Seats
                      var q=t.split(',')
                      console.log(q)
                      console.log(q.length)
                      for (y in q){
                        console.log(q[y])
                        e=q[y]
                        if (e!=""){
                          var p=document.getElementById(e).id;
                          console.log(p);
                          document.getElementById(p).classList.toggle('occupied');
                        }
                      }  
                    }
                  }
                }
                else if (ticketTrip=="Kota Station to Township"){
                  var mu=r.day["BookedSeats7"]
                  console.log(mu)
                  for (c in mu){
                    var iop=mu[c].date
                    console.log(iop)
                    if (iop==Datee.value){
                      console.log(mu[c].Seats)
                      t=mu[c].Seats
                      var q=t.split(',')
                      console.log(q)
                      console.log(q.length)
                      for (y in q){
                        console.log(q[y])
                        e=q[y]
                        if (e!=""){
                          var p=document.getElementById(e).id;
                          console.log(p);
                          document.getElementById(p).classList.toggle('occupied');
                        }
                      }  
                    }
                  }
                }
                
                break;
  
    default:
      break;
  }
})
// Save selected Trip index and Trip

// function setTripData(TripIndex, TripTrip) {
//   localStorage.setItem('selectedTripIndex', TripIndex);
//   localStorage.setItem('selectedTripTrip', TripTrip);
// }

// update total and count
function updateSelectedCount() {
  const selectedSeats = document.querySelectorAll('.rowX .seat.selected');
  // console.log(selectedSeats)
  var y=[];
  const seatsIndex = [...selectedSeats].map((seat) => [...seats].indexOf(seat));
  // console.log(seatsIndex)
  for(i=0; i<selectedSeats.length; i++){
    let x=selectedSeats[i].id;
    // console.log(x)
    y.push(x)
  }
  bookedSeats.value=y;
  // console.log(y)
  
Sb.addEventListener('click', ()=>{
  // if (Day.value=""){
  //   document.getElementById('alertDay').innerText="Please fill the form!"
  //   document.getElementById('alertDay').style.display="block";
  // }
  if (bookedSeats.value==""){
    document.getElementById('errors').innerText="Please select a Seat!"
    document.getElementById('errors').style.display="block";
    console.log("True")
}});


  // bookedSeats.value=seatsIndex;
  // localStorage.setItem('selectedSeats', JSON.stringify(seatsIndex));

  //copy selected seats into arr
  // map through array
  //return new array of indexes

  const selectedSeatsCount = selectedSeats.length;
  NumberOfSeats.value=selectedSeatsCount;
  // count.innerText = selectedSeatsCount;
  // total.innerText = selectedSeatsCount * ticketTrip;
}

// get data from localstorage and populate ui
// function populateUI() {
//   const selectedSeats = JSON.parse(localStorage.getItem('selectedSeats'));
//   if (selectedSeats !== null && selectedSeats.length > 0) {
//     seats.forEach((seat, index) => {
//       if (selectedSeats.indexOf(index) > -1) {
//         seat.classList.add('selected');
//       }
//     });
//   }

//   const selectedTripIndex = localStorage.getItem('selectedTripIndex');

//   if (selectedTripIndex !== null) {
//     TripSelect.selectedIndex = selectedTripIndex;
//   }
// }



// Seat click event
container.addEventListener('click', (e) => {
  if (e.target.classList.contains('seat') && !e.target.classList.contains('occupied')) {
    e.target.classList.toggle('selected');

    updateSelectedCount();
  }
});
// intial count and total
updateSelectedCount();