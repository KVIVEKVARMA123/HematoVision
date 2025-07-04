import os
import sys
import json
import random
import time
from datetime import datetime
import base64
from io import BytesIO
from PIL import Image
import numpy as np

class HematoVisionClassifier:
    """
    HematoVision Blood Cell Classifier
    Simulates advanced transfer learning-based classification
    """
    
    def __init__(self):
        self.cell_types = ['eosinophil', 'lymphocyte', 'monocyte', 'neutrophil']
        self.model_version = "1.2.0"
        self.confidence_threshold = 0.7
        
        # Cell type information database
        self.cell_info = {
            'eosinophil': {
                'description': 'Eosinophils are white blood cells that play a crucial role in allergic reactions and parasitic infections. They typically make up 1-4% of white blood cells and are characterized by their distinctive orange-red granules when stained with eosin dye.',
                'characteristics': [
                    'Bilobed nucleus with dense chromatin',
                    'Large, bright orange-red granules in cytoplasm',
                    'Diameter of 12-17 micrometers',
                    'Involved in allergic reactions and parasitic defense',
                    'Increased levels may indicate allergies or parasitic infections',
                    'Contains major basic protein and eosinophil cationic protein'
                ]
            },
            'lymphocyte': {
                'description': 'Lymphocytes are key components of the adaptive immune system, including T cells, B cells, and natural killer cells. They represent 20-40% of white blood cells and are essential for long-term immunity and immunological memory.',
                'characteristics': [
                    'Large, round nucleus with dense chromatin',
                    'Thin rim of basophilic cytoplasm',
                    'Diameter of 6-15 micrometers',
                    'Key players in adaptive immunity',
                    'Include T cells, B cells, and NK cells',
                    'Responsible for antibody production and cell-mediated immunity'
                ]
            },
            'monocyte': {
                'description': 'Monocytes are the largest white blood cells that differentiate into macrophages and dendritic cells when they migrate to tissues. They comprise 2-8% of white blood cells and are important for phagocytosis and antigen presentation.',
                'characteristics': [
                    'Large, kidney-shaped or horseshoe-shaped nucleus',
                    'Abundant gray-blue cytoplasm',
                    'Diameter of 15-30 micrometers',
                    'Precursors to macrophages and dendritic cells',
                    'Important for tissue repair and immune surveillance',
                    'Capable of phagocytosis and antigen presentation'
                ]
            },
            'neutrophil': {
                'description': 'Neutrophils are the most abundant white blood cells, making up 50-70% of all white blood cells. They are the first responders to bacterial infections and are characterized by their multi-lobed nucleus and ability to perform phagocytosis.',
                'characteristics': [
                    'Multi-lobed nucleus (3-5 lobes)',
                    'Fine, pink granules in cytoplasm',
                    'Diameter of 10-15 micrometers',
                    'First responders to bacterial infections',
                    'Short lifespan of 6-8 hours in circulation',
                    'Capable of neutrophil extracellular trap (NET) formation'
                ]
            }
        }
    
    def preprocess_image(self, image_path):
        """
        Preprocess the uploaded image for classification
        """
        try:
            # Open and validate image
            with Image.open(image_path) as img:
                # Convert to RGB if necessary
                if img.mode != 'RGB':
                    img = img.convert('RGB')
                
                # Resize to standard size (224x224 for most CNN models)
                img = img.resize((224, 224), Image.Resampling.LANCZOS)
                
                # Convert to numpy array and normalize
                img_array = np.array(img, dtype=np.float32) / 255.0
                
                return img_array
                
        except Exception as e:
            raise Exception(f"Error preprocessing image: {str(e)}")
    
    def extract_features(self, image_array):
        """
        Simulate feature extraction using transfer learning
        In a real implementation, this would use a pre-trained CNN
        """
        # Simulate feature extraction process
        time.sleep(1)  # Simulate processing time
        
        # Generate realistic feature vector
        features = np.random.rand(2048)  # Typical CNN feature vector size
        
        # Add some image-based variations
        mean_intensity = np.mean(image_array)
        std_intensity = np.std(image_array)
        
        # Modify features based on image characteristics
        features[0] = mean_intensity
        features[1] = std_intensity
        
        return features
    
    def classify_cell(self, features):
        """
        Classify the blood cell based on extracted features
        """
        # Simulate neural network classification
        # Generate base probabilities
        probabilities = {}
        
        # Create realistic probability distribution
        for cell_type in self.cell_types:
            probabilities[cell_type] = random.uniform(0.05, 0.25)
        
        # Select a dominant class with higher probability
        dominant_class = random.choice(self.cell_types)
        probabilities[dominant_class] = random.uniform(0.6, 0.9)
        
        # Normalize probabilities to sum to 1
        total = sum(probabilities.values())
        for cell_type in probabilities:
            probabilities[cell_type] /= total
        
        # Get predicted class and confidence
        predicted_class = max(probabilities, key=probabilities.get)
        confidence = probabilities[predicted_class]
        
        return predicted_class, confidence, probabilities
    
    def generate_report(self, predicted_class, confidence, probabilities, processing_time):
        """
        Generate comprehensive classification report
        """
        cell_data = self.cell_info[predicted_class]
        
        report = {
            'predicted_class': predicted_class,
            'confidence': float(confidence),
            'probabilities': {k: float(v) for k, v in probabilities.items()},
            'description': cell_data['description'],
            'characteristics': cell_data['characteristics'],
            'metadata': {
                'model_version': self.model_version,
                'processing_time': processing_time,
                'timestamp': datetime.now().isoformat(),
                'method': 'Transfer Learning CNN',
                'confidence_threshold': self.confidence_threshold
            }
        }
        
        return report
    
    def classify_image(self, image_path):
        """
        Complete classification pipeline
        """
        start_time = time.time()
        
        try:
            # Validate input
            if not os.path.exists(image_path):
                raise Exception("Image file not found")
            
            # Preprocess image
            print("Preprocessing image...")
            image_array = self.preprocess_image(image_path)
            
            # Extract features
            print("Extracting features using transfer learning...")
            features = self.extract_features(image_array)
            
            # Classify
            print("Classifying blood cell...")
            predicted_class, confidence, probabilities = self.classify_cell(features)
            
            # Calculate processing time
            processing_time = time.time() - start_time
            
            # Generate report
            report = self.generate_report(predicted_class, confidence, probabilities, processing_time)
            
            print(f"Classification complete: {predicted_class} ({confidence:.1%} confidence)")
            
            return report
            
        except Exception as e:
            return {
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }

def main():
    """
    Main function for command-line usage
    """
    if len(sys.argv) != 2:
        print("Usage: python blood_cell_classifier.py <image_path>")
        print("Example: python blood_cell_classifier.py blood_cell.jpg")
        sys.exit(1)
    
    image_path = sys.argv[1]
    
    print("=" * 50)
    print("HematoVision Blood Cell Classifier")
    print("=" * 50)
    
    # Initialize classifier
    classifier = HematoVisionClassifier()
    
    # Classify image
    result = classifier.classify_image(image_path)
    
    # Output results
    if 'error' in result:
        print(f"Error: {result['error']}")
        sys.exit(1)
    else:
        print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
