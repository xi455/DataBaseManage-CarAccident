
    function updateMap() {
            var selectedYear = document.getElementById('yearSelect').value;

            // Make an AJAX request to send selectedYear to views.py
            fetch(`/map/api/map/data/?year=${selectedYear}`)
                .then(response => response.json())
                .then(data => {
                    document.getElementById('map').innerHTML = data.map_html;
                })
                .catch(error => console.error('Error:', error));
        }