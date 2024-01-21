document.addEventListener("DOMContentLoaded", function () {
    // Sample data for the attendance chart
    const chartData = {
        labels: ["January", "February", "March", "April", "May", "June"],
        datasets: [
            {
                label: "Attendance Percentage",
                backgroundColor: "rgba(75, 192, 192, 0.2)",
                borderColor: "rgba(75, 192, 192, 1)",
                borderWidth: 1,
                data: [65, 59, 80, 81, 56, 70],
            },
        ],
    };

    // Get the canvas element
    const attendanceChartCanvas = document.getElementById("attendanceChart");

    if (attendanceChartCanvas) {
        // Create the attendance chart
        const attendanceChart = new Chart(attendanceChartCanvas, {
            type: "bar",
            data: chartData,
            options: {
                responsive: true,
                scales: {
                    y: {
                        beginAtZero: true,
                        max: 100,
                        title: {
                            display: true,
                            text: "Percentage",
                        },
                    },
                    x: {
                        title: {
                            display: true,
                            text: "Months",
                        },
                    },
                },
            },
        });
    }
});
