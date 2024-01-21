// Add your JavaScript code here
// Fetch attendance analysis data from the server and render the chart
function fetchAndRenderAnalysis() {
    // Fetch data from server
    $.get('/attendance_analysis')
    .done(function(response) {
      // Render the chart
      renderAnalysisChart(response.total_members, response.present_members);
    })
    .fail(function(error) {
      console.log('Error fetching attendance analysis:', error);
    });
  }
  
  // Render attendance analysis chart using Chart.js
  function renderAnalysisChart(totalMembers, presentMembers) {
    var ctx = document.getElementById('analysisChart').getContext('2d');
    var analysisChart = new Chart(ctx, {
      type: 'doughnut',
      data: {
        labels: ['Present', 'Absent'],
        datasets: [{
          data: [presentMembers, totalMembers - presentMembers],
          backgroundColor: ['#66b3ff', '#ff9999']
        }]
      }
    });
  }
  
  // Fetch and render attendance analysis when the page loads
  document.addEventListener('DOMContentLoaded', fetchAndRenderAnalysis);
  // Add your JavaScript code here
function generateReport() {
    // You can use AJAX or other methods to fetch report data from the server
    // Example AJAX code using jQuery
    $.get('/generate_report')
    .done(function(response) {
      document.getElementById('reportContainer').innerHTML = response.report;
    })
    .fail(function(error) {
      console.log('Error fetching report:', error);
    });
  }

  // Add your JavaScript code here
function markAttendance() {
    const face_id = document.getElementById('face_id').value;
  
    // You can use AJAX or other methods to send the data to the server to mark attendance
    // Example AJAX code using jQuery
    $.post('/mark_attendance', {
      face_id: face_id
    })
    .done(function(response) {
      document.getElementById('attendanceMessage').innerHTML = response.message;
      // Clear form field after successful attendance marking
      document.getElementById('face_id').value = '';
    })
    .fail(function(error) {
      document.getElementById('attendanceMessage').innerHTML = error.responseJSON.error;
    });
  }
  // Add your JavaScript code here
function registerMember() {
    const name = document.getElementById('name').value;
    const phone_number = document.getElementById('phone_number').value;
    const residence = document.getElementById('residence').value;
    const age = document.getElementById('age').value;
  
    // You can use AJAX or other methods to send the data to the server for registration
    // Example AJAX code using jQuery
    $.post('/register_member', {
      name: name,
      phone_number: phone_number,
      residence: residence,
      age: age
    })
    .done(function(response) {
      document.getElementById('registrationMessage').innerHTML = response.message;
      // Clear form fields after successful registration
      document.getElementById('name').value = '';
      document.getElementById('phone_number').value = '';
      document.getElementById('residence').value = '';
      document.getElementById('age').value = '';
    })
    .fail(function(error) {
      document.getElementById('registrationMessage').innerHTML = error.responseJSON.error;
    });
  }
  
  
  