async function fetchBuilds(limit=10) {
    const el = document.getElementById("buildList");
    el.innerHTML = "Loading...";

    try {
        const res = await fetch(`/api/jenkins/builds?limit=${limit}`);
        const data = await res.json();

        if (data.error) {
            el.innerHTML = "<div class='error'>Jenkins error: " + data.error + "</div>";
            return;
        }

        el.innerHTML = data.map(b => `
            <div class="build-row ${b.result}">
                <span>#${b.number}</span>
                <span>${b.result}</span>
                <span>${b.duration_sec}s</span>
            </div>
        `).join("");

    } catch (err) {
        el.innerHTML = "Failed: " + err;
    }
}

window.onload = () => {
    fetchBuilds();
    setInterval(fetchBuilds, 15000);
};
