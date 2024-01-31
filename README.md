### HTML Files
- **index.html**:
  - Serves as the main page of the game.
  - Contains the game's start button to begin playing and a welcome or instructional message.
  - Includes the snake's initial position and orientation in the cave.


### Routes

- **@app.route('/'):**
  - Binds the root URL '/' to the corresponding view function.
  - Typically renders the 'index.html' template, which displays the game interface.


- **@app.route('/game'):**
  - Represents the actual game mechanics.
  - Handles user input for snake movement direction.
  - Depending on the direction, it updates the snake's position and checks for collisions with walls, treats, and itself.
  - Updates the game state, player score, and relevant information.
  - Returns a JSON response with the updated game state.


- **@app.route('/score'):**
  - Handles requests to retrieve the player's current score.
  - Returns the score as a JSON response.