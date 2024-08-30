<template>
  <div class="modal-overlay text-black" @click.self="closeModal">
    <div class="modal-content">
      <!-- Header Section -->
      <div class="modal-header">
        <button class="close-button" @click="closeModal">✕</button>
      </div>
      <!-- Date Selection -->
      <div class="date-selection">
        <button v-for="(date, index) in dates" :key="index" @click="selectDate(date)"
          :class="{ 'active-date': selectedDate === date }">
          {{ date }}
        </button>
      </div>
      <!-- Location and Format Selection -->
      <div class="location-format">
        <div class="location-tabs">
          <button v-for="(location, index) in locations" :key="index" @click="selectLocation(location)"
            :class="{ 'active-tab': selectedLocation === location }">
            {{ location }}
          </button>
        </div>
        <div class="format-tabs">
          <button v-for="(format, index) in formats" :key="index" @click="selectFormat(format)"
            :class="{ 'active-format': selectedFormat === format }">
            {{ format }}
          </button>
        </div>
      </div>
      <!-- Time Slot Selection -->
      <div class="time-slots">
        <div v-for="(time, index) in times" :key="index" class="time-slot">
          <span>{{ time }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    id: {
      type: Number,
      required: true
    }
  },
  data() {
    return {
      dates: ['05 Thu', '06 Fri', '07 Sat', '08 Sun'], // Example dates
      locations: ['California', 'New York'], // Example locations
      formats: ['3D', '2D'], // Example formats
      times: ['7:30 am', '8:30 am', '2:30 pm'], // Example time slots
      selectedDate: '05 Thu',
      selectedLocation: 'California',
      selectedFormat: '3D'
    };
  },
  methods: {
    closeModal() {
      this.$emit('close');
    },
    selectDate(date) {
      this.selectedDate = date;
    },
    selectLocation(location) {
      this.selectedLocation = location;
    },
    selectFormat(format) {
      this.selectedFormat = format;
    }
  }
};
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal-content {
  background-color: #fff;
  width: 90%;
  max-width: 600px;
  padding: 20px;
  border-radius: 8px;
}

.modal-header {
  display: flex;
  justify-content: flex-end;
}

.close-button {
  background: none;
  border: none;
  font-size: 1.5rem;
  cursor: pointer;
}

.date-selection {
  display: flex;
  justify-content: space-between;
  margin-bottom: 15px;
}

.date-selection button {
  background: none;
  border: none;
  padding: 10px;
  cursor: pointer;
}

.active-date {
  font-weight: bold;
}

.location-format {
  display: flex;
  justify-content: space-between;
  margin-bottom: 15px;
}

.location-tabs,
.format-tabs {
  display: flex;
}

.location-tabs button,
.format-tabs button {
  background: none;
  border: none;
  padding: 10px;
  cursor: pointer;
}

.active-tab,
.active-format {
  font-weight: bold;
}

.time-slots {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.time-slot {
  padding: 10px;
  background: #f0f0f0;
  border-radius: 4px;
  text-align: center;
}
</style>