
# Import necessary libraries
from flask import Flask, render_template, request, jsonify
import random

# Initialize the Flask app
app = Flask(__name__)

# Define the game state
game_state = {
    'snake': [
        [5, 5],
        [4, 5],
        [3, 5],
    ],
    'treats': [],
    'direction': 'right',
    'score': 0,
    'game_over': False,
}

# Generate initial treats
for _ in range(10):
    game_state['treats'].append([random.randint(0, 10), random.randint(0, 10)])

# Define the main route
@app.route('/')
def index():
    return render_template('index.html')

# Define the game route
@app.route('/game')
def game():
    # Get the user input for the next direction
    direction = request.args['direction']

    # Update the snake's direction
    if direction in ['up', 'down', 'left', 'right']:
        game_state['direction'] = direction

    # Update the snake's position
    head = game_state['snake'][0]
    if game_state['direction'] == 'up':
        head[1] -= 1
    elif game_state['direction'] == 'down':
        head[1] += 1
    elif game_state['direction'] == 'left':
        head[0] -= 1
    elif game_state['direction'] == 'right':
        head[0] += 1

    # Check for collisions
    if head in game_state['snake'][1:]:
        # Snake hit itself
        game_state['game_over'] = True
    elif head[0] < 0 or head[0] > 10 or head[1] < 0 or head[1] > 10:
        # Snake hit a wall
        game_state['game_over'] = True
    else:
        # Check for eating a treat
        if head in game_state['treats']:
            # Snake ate a treat
            game_state['score'] += 1
            game_state['treats'].remove(head)
            # Generate a new treat
            game_state['treats'].append([random.randint(0, 10), random.randint(0, 10)])

        # Move the snake
        game_state['snake'].insert(0, head)
        game_state['snake'].pop()

    # Return the game state
    return jsonify(game_state)

# Define the score route
@app.route('/score')
def score():
    # Return the player's score
    return jsonify({'score': game_state['score']})

# Run the app
if __name__ == '__main__':
    app.run()
