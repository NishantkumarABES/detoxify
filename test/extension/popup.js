document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('preferencesForm');
  
    form.addEventListener('submit', function (event) {
      event.preventDefault(); // Prevent the form from submitting the traditional way
  
      const interests = document.getElementById('interests').value;
      const dislikes = document.getElementById('dislikes').value;
  
      // Save preferences using Chrome storage API
      chrome.storage.sync.set({
        interests: interests,
        dislikes: dislikes
      }, function () {
        console.log('Preferences saved:', { interests, dislikes });
      });
  
      // Optionally provide feedback to the user
      alert('Preferences saved!');
    });
  });
  