# Building-dataset
Deep Learning model for building detection 
Dataset Collection and Preprocessing:
Data Collection: High-resolution remote sensing imagery of the Wuhan region was sourced. The dataset consisted of satellite and UAV images with high spatial resolution.
Data Format and Conversion: Due to the large size of the dataset, high-resolution images were converted to the JPEG2 format for easier handling and processing.
Tiling for Efficient Download: To manage the large dataset, tiling techniques were applied to divide the images into smaller sections, allowing for faster downloading and processing.
Annotation Using EISeg Tool: The EISeg tool was used to annotate the dataset, generating semantic and instance-level labels for rooftop detection. The tool was configured with pre-defined models for optimal annotation.
Data Resizing: Images were resized to a consistent size to ensure uniformity during training and testing. This step involved balancing spatial resolution with computational efficiency.
Data Splitting and Organization:
Training, Validation, and Test Set Division: The dataset was split into three subsets: 70% for training, 15% for validation, and 15% for testing. This was done to ensure balanced representation and avoid overfitting.
Data Preprocessing: During preprocessing, all images were standardized, ensuring consistent sizes and naming conventions across the dataset. Various augmentation techniques, including resizing and flipping, were applied to enhance model robustness.
Model Selection: Several deep-learning models were selected for rooftop detection, including PP-LiteSeg, ANN, DANet, and DeepLabV3.
Hyperparameter Setting: Hyperparameters such as learning rate, batch size, and optimizer choice (e.g., SGD) were carefully set for each model ( see yml file in Data directory)
Model Architecture: Predefined backbones such as ResNet50 and ResNet101 were used with customized layers to ensure effective feature extraction for rooftop detection.
Model Training: The deep learning models were trained on the labeled dataset, with continuous evaluation using the validation set to prevent overfitting.
Loss Functions: Cross-entropy loss was primarily used, with adjustments made for class imbalances using techniques such as Online Hard Example Mining (OHEM) for models like DANet.
Optimization: The models were trained using the stochastic gradient descent (SGD) optimizer, with the learning rate adjusted according to the polynomial decay schedule.
Model Evaluation:
Performance Metrics: The performance of each model was evaluated using metrics such as Intersection over Union (IoU), accuracy, and F1-score. These metrics provided insights into the model’s ability to accurately detect rooftops.
Comparative Analysis: The results of all models were compared to determine the most effective architecture for rooftop detection in the Wuhan dataset.
Result in Integration and Post-Processing:
GDAL Mosaic Algorithm: After the models completed their predictions on tiled sections, the results were combined using the GDAL mosaic algorithm to generate a seamless output, ensuring the integration of predictions across all image tiles.
Final Adjustment and Scaling: The final predictions were scaled and organized into separate folders to ensure uniform image sizes and consistency across all predictions. The final dataset was ready for post-analysis and use.
Interactive versions of the Hongshan maps shp and images with lables dataset  shown in this manuscript are available under https://drive.google.com/drive/folders/13rfYYYY2fDMAF0eZTPQaiFzxF-JzhXmI?usp=drive_link

