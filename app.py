import os
import random
import gradio as gr

def perform_search(text_query, image_query, weight, use_pca, pca_components):
    """
    Perform a search query combining text and image inputs.

    Args:
        text_query (str): The text query.
        image_query (numpy array): The uploaded image (optional).
        weight (float): Weight for the text query (0-1).
        use_pca (bool): Whether to use PCA for image embeddings.
        pca_components (int): Number of principal components if PCA is used.

    Returns:
        list: A list of [image_path, caption] pairs for the Gradio Gallery.
    """
    # List all available images in the directory
    image_folder = "coco_images_resized"
    all_images = os.listdir(image_folder)
    
    # Randomly select 5 images for demonstration purposes
    selected_images = random.sample(all_images, 5)
    
    # Generate results
    results = [
        {
            "image": os.path.abspath(os.path.join(image_folder, image_name)),
            "caption": f"Similarity: {1.0 - 0.1 * i:.2f}"  # Dummy similarity score
        }
        for i, image_name in enumerate(selected_images)
    ]
    
    # Debug: Print generated image paths
    for result in results:
        print(f"Generated image path: {result['image']}")
    
    # Return formatted results for Gradio Gallery
    return [[result["image"], result["caption"]] for result in results]

def main():
    interface = gr.Interface(
        fn=perform_search,  # Function to process queries
        inputs=[
            gr.Textbox(label="Text Query"),
            gr.Image(type="numpy", label="Image Query (optional)"),
            gr.Slider(0, 1, value=0.5, label="Weight for Text Query (0.0-1.0)"),
            gr.Checkbox(label="Use PCA for Image Query"),
            gr.Number(value=50, label="Number of Principal Components (if PCA enabled)")
        ],
        outputs=gr.Gallery(label="Search Results"),  # Updated output
        title="Simplified Google Image Search",
    )
    interface.launch()

if __name__ == "__main__":
    main()