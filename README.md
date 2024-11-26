# GenAI-Experiments

## ChefGPT

ChefGPT is an interactive AI-powered assistant designed to help users create healthy and delicious vegetarian dishes. It specializes in soups and salads, providing ingredient-based suggestions, recipe critiques, and cooking tips.

### Features

- **Ingredient-Based Suggestions**: Provides dish names based on user-provided ingredients.
- **Recipe Generation**: Offers full recipes only when specifically requested for recognized dishes.
- **Cooking Tips**: Shares helpful tips and tricks for food preparation and cooking techniques.
- **Recipe Critiques**: Analyzes user-provided recipes and suggests improvements.

### Requirements

- Python 3.x
- OpenAI Python client library
- An OpenAI API key

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ChefGPT.git
   cd ChefGPT
   ```

2. Install the required packages:
   ```bash
   pip install openai
   ```

3. Set your OpenAI API key as an environment variable:
   ```bash
   export OPENAI_API_KEY="your_api_key_here"
   ```

### Usage

1. Run the script:
   ```bash
   python Generative-AI-Applications/Projects/ChefGPT.py
   ```

2. Follow the prompts to interact with ChefGPT. You can ask for healthy dish suggestions, request recipes, or seek cooking advice.

### Example Interaction

**ChefGPT:** Hi. I am the new chef in town. How can I help you make your life healthier and happier?

**User:** suggest dish using beet and carrot  
**ChefGPT:** A beautiful and healthy dish you can prepare using beets and carrots is a **Beet and Carrot Salad**. 

For this salad, you can roast the beets and grate the carrots for a vibrant, colorful presentation. Add a dressing made from olive oil, lemon juice, salt, and a touch of honey or maple syrup for sweetness. Incorporate some fresh herbs like parsley or mint for added flavor. 

You could also consider adding some feta cheese for creaminess, or nuts like walnuts for crunch. This dish combines earthy flavors and is both refreshing and nutritious, perfect for a light meal or a side! Let me know if you'd like more specific details or variations!

---

**User:** suggest recipe for marmalade  
**ChefGPT:** I appreciate your interest in marmalade, but unfortunately, it falls outside my specialty of healthy soups and salads. If you're looking for something delightful and nutritious that features fruits and vegetables, let me know! I’d be happy to help you with a related recipe or suggestion!

---

**User:** suggest recipe for machow soup  
**ChefGPT:** I appreciate your interest in Machow soup, but unfortunately, it falls outside my expertise in healthy vegetarian soups and salads. However, I can suggest a delicious and nutritious vegetarian soup that you might enjoy! 

How about a **Roasted Tomato and Basil Soup**? This soup is made with ripe tomatoes, fresh basil, garlic, and a hint of balsamic vinegar for depth of flavor. It’s hearty and packed with nutrients. If you're interested, I can provide more details or variations for this soup! Let me know!

---

**User:** Yes that is fine  
**ChefGPT:** Great choice! Here's a simple and delicious recipe for **Roasted Tomato and Basil Soup**:

**Ingredients:**
- 2 pounds ripe tomatoes (halved)
- 1 onion (chopped)
- 4 cloves garlic (peeled)
- 3 tablespoons olive oil
- Salt and pepper to taste
- 1 cup fresh basil leaves
- 2 cups vegetable broth
- 1 tablespoon balsamic vinegar (optional)
- A pinch of sugar (optional, to balance acidity)

**Instructions:**

1. **Roast the Tomatoes:**
   - Preheat your oven to 400°F (200°C).
   - On a baking sheet, place the halved tomatoes and garlic cloves. Drizzle with olive oil, and season with salt and pepper.
   - Roast in the oven for about 25-30 minutes or until the tomatoes are caramelized.

2. **Sauté the Onions:**
   - In a large pot, heat a bit of olive oil over medium heat. Add the chopped onion and sauté until translucent.

3. **Combine Ingredients:**
   - Once the tomatoes are roasted, add them to the pot along with the garlic, fresh basil leaves, and vegetable broth.
   - Bring the mixture to a simmer, and let it cook for about 10-15 minutes to meld the flavors.

4. **Blend the Soup:**
   - Use an immersion blender to puree the soup until smooth. If you don’t have one, carefully transfer the mixture to a blender (in batches if necessary), then return it to the pot.

5. **Finish the Soup:**
   - Stir in the balsamic vinegar and taste your soup. Adjust the seasoning and add a pinch of sugar if it's too acidic.

6. **Serve:**
   - Ladle the soup into bowls and garnish with additional fresh basil or a drizzle of olive oil.

This soup is warming, comforting, and packed with flavor. Serve it alongside a slice of whole-grain bread for a complete meal! Let me know if you have any questions or need any substitutions. Enjoy your cooking!

