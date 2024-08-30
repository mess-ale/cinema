<template>
    <div class="showtimes-table">
      <h2>Showtimes</h2>
      <table>
        <thead>
          <tr>
            <th>Date</th>
            <th>Time</th>
            <th>Format</th>
            <th>Availability</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(showtime, index) in showtimes" :key="index">
            <td>{{ showtime.date }}</td>
            <td>{{ showtime.time }}</td>
            <td>{{ showtime.format }}</td>
            <td :class="{'available': showtime.availability === 'Available', 'sold-out': showtime.availability === 'Sold Out'}">
              {{ showtime.availability }}
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  
  <script>
  export default {
    name: 'ShowtimesTable',
    data() {
      return {
        showtimes: [
          { date: 'Dec 20', time: '7:00PM', format: '3D', availability: 'Available' },
          { date: 'Dec 20', time: '10:00PM', format: 'IMAX', availability: 'Available' },
          { date: 'Dec 21', time: '12:00PM', format: 'Standard', availability: 'Sold Out' },
          { date: 'Dec 21', time: '3:00PM', format: 'Standard', availability: 'Available' },
          { date: 'Dec 21', time: '6:00PM', format: '3D', availability: 'Sold Out' }
        ]
      }
    }
  }
  </script>
  
  <style scoped>
  .showtimes-table {
    padding: 20px;
    background-color: #1c1c1e;
    border-radius: 8px;
    color: #ffffff;
  }
  
  .showtimes-table h2 {
    margin-bottom: 20px;
    color: #ffffff;
  }
  
  table {
    width: 100%;
    border-collapse: collapse;
  }
  
  th, td {
    padding: 10px;
    text-align: left;
    border-bottom: 1px solid #444;
  }
  
  th {
    background-color: #2c2c2e;
    color: #8e8e93;
  }
  
  td {
    background-color: #2c2c2e;
    color: #ffffff;
  }
  
  .available {
    background-color: theme('colors.secondary') ;
    color: #ffffff;
    border-radius: 4px;
    padding: 5px 10px;
    text-align: center;
  }
  
  .sold-out {
    background-color: theme('colors.primary');
    color: #ffffff;
    border-radius: 4px;
    padding: 5px 10px;
    text-align: center;
  }
  </style>
  