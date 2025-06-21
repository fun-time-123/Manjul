async function analyzeStock() {
    const stock = document.getElementById("stockInput").value;
    const response = await fetch(`https://manjul-1.onrender.com/analyze?stock=${stock}`);
    const data = await response.json();
    document.getElementById("output").textContent = JSON.stringify(data, null, 2);
}
