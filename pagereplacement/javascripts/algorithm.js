function toggle() {
  if (document.documentElement.style.getPropertyValue("--bg") == "white") {
    document.documentElement.style.setProperty("--bg", "black");
    document.documentElement.style.setProperty("--clr", "white");
  } else {
    document.documentElement.style.setProperty("--bg", "white");
    document.documentElement.style.setProperty("--clr", "black");
  }
}
function press() {
  const val = document.getElementById("rs").value.split(" ");
}
async function Calculate() {
  let capacity = document.getElementById("capacity").value;
  let referenceString = document.getElementById("rs").value;
  if(!capacity || !referenceString) return alert("Please fill all the fields");
  let referenceStringArray = referenceString.split(" ").filter(item => item !== '');
  console.log(referenceStringArray)
  let pageFaultsFifo = 0;
  pageFaultsFifo = await eel.Algorithm('fifo', capacity, referenceStringArray)();
  let pageFaultsLru = 0;
  pageFaultsLru = await eel.Algorithm('lru', capacity, referenceStringArray)();
  let missFifo = pageFaultsFifo[0];
  let missLru = pageFaultsLru[0];
  let hitFifo = referenceStringArray.length - pageFaultsFifo[0];
  let hitLru = referenceStringArray.length - pageFaultsLru[0];
  let missRateFifo = (missFifo / referenceStringArray.length) * 100;
  let missRateLru = (missLru / referenceStringArray.length) * 100;
  let hitRateFifo = (hitFifo / referenceStringArray.length) * 100;
  let hitRateLru = (hitLru / referenceStringArray.length) * 100;
  let pageFaultsLifo = 0;
  pageFaultsLifo = await eel.Algorithm('lifo', capacity, referenceStringArray)();
  let missLifo = pageFaultsLifo[0];
  let hitLifo = referenceStringArray.length - pageFaultsLifo[0];
  let missRateLifo = (missLifo / referenceStringArray.length) * 100;
  let hitRateLifo = (hitLifo / referenceStringArray.length) * 100;
  document.getElementById("LifoPageFaults").innerHTML = pageFaultsLifo[0];
  document.getElementById("LifoPageHits").innerHTML = referenceStringArray.length - pageFaultsLifo[0];
  document.getElementById("LifoPageFaultRatio").innerHTML = missRateLifo.toFixed(2) + "%";
  document.getElementById("LifoPageHitRatio").innerHTML = hitRateLifo.toFixed(2) + "%";
  document.getElementById("LifoImg").src = pageFaultsLifo[1];

  document.getElementById("fifoPageFaults").innerHTML = pageFaultsFifo[0];
  document.getElementById("fifoPageHits").innerHTML = referenceStringArray.length - pageFaultsFifo[0];
  document.getElementById("FifoImg").src = pageFaultsFifo[1];
  document.getElementById("fifoPageFaultRatio").innerHTML = missRateFifo.toFixed(2) + "%";
  document.getElementById("fifoPageHitRatio").innerHTML = hitRateFifo.toFixed(2) + "%";
  document.getElementById("lruPageFaults").innerHTML = pageFaultsLru[0];
  document.getElementById("lruPageHits").innerHTML = referenceStringArray.length - pageFaultsLru[0];
  document.getElementById("lruPageFaultRatio").innerHTML = missRateLru.toFixed(2) + "%";
  document.getElementById("lruPageHitRatio").innerHTML = hitRateLru.toFixed(2) + "%";
  document.getElementById("LruImg").src = pageFaultsLru[1];
  document.querySelectorAll(".holder").forEach(item => {
    item.style.display = "flex";
  });


}
