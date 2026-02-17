# Building a Classification Network

In this lab, we will work with the UNSW-NB15 dataset, a popular benchmark for network intrusion detection. It consists of raw network traffic data captured in a controlled environment.

The data includes a mix of normal network activity and nine types of cyberattacks, such as:

- DoS (Denial of Service): Attempts to shut down a machine or network.
- Worms: Malware that replicates itself to spread to other computers.
- Fuzzers: Automated software testing techniques often used by attackers to find vulnerabilities.
- Reconnaissance: Probing a network to find weaknesses.

Your Goal: Build a Neural Network that can look at a single packet or flow of traffic and correctly classify it as either "Normal" or one of the specific attack types.

Deep Learning pipelines have many moving parts. If you try to build the perfect pipeline from line one—with complex normalization, advanced architecture, and perfect regularization—debugging becomes impossible when it inevitably breaks.

Instead, we will follow an iterative engineering workflow:

- The Naive Pipeline: We will first build the simplest possible pipeline that runs without crashing. We will load the data, convert text to numbers, and feed it into a network.
- Diagnosis: We will look at the results (which will likely be poor) and diagnose why the network failed.
- We will introduce specific techniques one by one to solve these problems and watch performance improve.

You will work in a scratch notebook, and then assemble a final draft to turn in with answers to asked questions, the best version of your model, and an explanation of your process.

## Data Exploration

To start, download the data. [Go here](https://unsw-my.sharepoint.com/personal/z5025758_ad_unsw_edu_au/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fz5025758%5Fad%5Funsw%5Fedu%5Fau%2FDocuments%2FUNSW%2DNB15%20dataset%2FCSV%20Files&viewid=f8d1dec5%2Dcd5f%2D42ae%2D8b06%2D2fece580c74a), and download `NUSW-NB15_features.csv`. Then download both files in the `Training and Testing Sets` folder. Put all that within a folder in the `/SD312` directory (note, that's not in your home directory, that's off of root). This folder is on the hard disk of the machine, rather than part of the networked file system - reading from it is faster, so this is a good place for our data.

Load the training and testing sets into pandas dataframes. Your labels are in column `attack_cat`. **What is the percentage of datapoints in each of the `attack_cat` categories, for each of the datasets? If the network was lazy and just predicted the most common class, what percentage accuracy would it get?**

**In terms of your data, which columns are *numerical* and which are *categorical*? Are all the columns about the same scale (in terms of mean, and min-max), or are some big, and others small?** The `NUSW-NB15_features.csv` and [`.describe()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html) are among the helpful tools that will help with this.

## Creating the Pipeline

To make our first attempt, we need to make `Dataset`s, `DataLoader`s, and a simple neural network.

### PyTorch Datasets

Below is code for making your dataset. Your instructor will go over it with you. If later you need to recall what is happening here, feel free to paste it into Gemini for an explanation. You should understand this code.

```python
class CSVDataset(Dataset):
    """
    Custom Dataset class for loading Network Intrusion Detection data from CSV.
    Handles loading, cleaning, One-Hot Encoding, and Tensor conversion.
    """
    def __init__(self, file_path, categorical_cols, encoder, is_train=True):
        """
        Args:
            file_path (string): Path to the CSV file.
            categorical_cols (list): List of column names containing text data to encode.
            encoder (OneHotEncoder): The sklearn encoder instance.
            is_train (bool): If True, the encoder learns from this data (fits).
                             If False, it uses previously learned categories (transforms).
        """
        # 1. Load Data
        df = pd.read_csv(file_path)
        
        # 2. Extract Labels
        # We separate the target ('attack_cat') immediately so we don't accidentally
        # include it as an input feature (which would be cheating/leakage).
        labels = df['attack_cat']
        
        # Drop columns we don't need or that are targets
        # 'label' is the binary target (0/1), 'id' is useless for learning
        df.drop(columns=['attack_cat', 'label', 'id'], inplace=True)

        # 3. Feature Splitting
        # We need to process text (categorical) and numbers (numerical) differently.
        cat_data = df[categorical_cols]
        num_data = df.drop(columns=categorical_cols)

        # 4. One-Hot Encoding
        # Neural Networks cannot read text. We convert categories into binary vectors.
        if is_train:
            # TRAINING MODE: The encoder looks at the data, learns the unique categories,
            # and then transforms the text into numbers (Fit & Transform).
            encoded_cats = encoder.fit_transform(cat_data)
        else:
            # TESTING MODE: The encoder uses ONLY the categories it learned during training.
            # It does NOT learn new categories here. If a new category appears, 
            # 'handle_unknown=ignore' prevents a crash. This prevents Data Leakage.
            encoded_cats = encoder.transform(cat_data)

        # 5. Data Reassembly
        # Turn the encoded output back into a Pandas DataFrame
        encoded_df = pd.DataFrame(encoded_cats, index=df.index)
        
        # Concatenate the original numerical columns with the new encoded binary columns
        df_final = pd.concat([num_data, encoded_df], axis=1)

        # 6. Target Encoding
        # Convert string labels (e.g., 'DoS', 'Worms') into integers (e.g., 1, 2)
        self.label_encoder = LabelEncoder()
        target_integers = self.label_encoder.fit_transform(labels)
        
        # 7. Convert to PyTorch Tensors
        # Inputs must be float32 (for matrix multiplication)
        # Targets (for CrossEntropyLoss) must be long (integers)
        self.x = torch.tensor(df_final.values, dtype=torch.float32)
        self.y = torch.tensor(target_integers, dtype=torch.long)
        
        self.n_samples = df_final.shape[0]
        self.num_features = df_final.shape[1] # Save this to define the Neural Net input layer size

    def __getitem__(self, index):
        # This method allows the DataLoader to retrieve one sample at a time
        return self.x[index], self.y[index]

    def __len__(self):
        # This tells the DataLoader how many total samples exist
        return self.n_samples

    def get_class_name(self, label_id):
        # Helper function to convert a predicted integer back to a string name (e.g., 1 -> 'DoS')
        return self.label_encoder.inverse_transform([label_id])[0]

# Define which columns are text-based and need encoding
categorical_cols = #TODO: create a list of column names that contain categorical data

# Initialize the encoder once. 
# sparse_output=False ensures we get a dense array (easier to use with pandas).
# handle_unknown='ignore' protects us if the test set has a protocol we didn't see in training.
encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')

# Create the Datasets
# Note: is_train=True for training (fitting the encoder) and is_train=False for testing (using the fitted encoder)
training_dataset = CSVDataset('/SD312/UNSW_NB15_training-set.csv', categorical_cols, encoder, is_train=True)
testing_dataset = CSVDataset('/SD312/UNSW_NB15_testing-set.csv', categorical_cols, encoder, is_train=False)
```

**Fill in the definition of `categorical_cols` with the column titles of columns containing categorical data.**

### DataLoaders

DataLoaders assemble random batches of data for training and testing from Datasets. The below code builds training and testing dataloaders. These dataloaders will:

- Assemble the next batch while the network is training on the previous batch, and
- Shuffle batches during training so each batch is randomly drawn from the whole dataset, rather than in the order they were stored (which may contain patterns).

```python
# Hyperparameter
BATCH_SIZE = 32 # For example

train_loader = DataLoader(
    dataset=trainingDS,
    batch_size=BATCH_SIZE,
    shuffle=True,        # Essential for training to prevent ordering bias
    pin_memory=True      # Speeds up host-to-device (CPU to GPU) transfers
)

test_loader = DataLoader(
    dataset=testingDS,
    batch_size=BATCH_SIZE,
    shuffle=False,       # Not necessary to shuffle validation/test data
    pin_memory=True
)
```

<div style="background-color: #fff3cd; border-left: 6px solid #ffc107; padding: 15px; color: #856404;">
  <strong>🟡 AI Policy: YELLOW</strong> <br>
  Generative AI is allowed, with limitations.
</div>

### Network

Create a simple neural net with appropriate input size (for your data) and output size (for your classification task).  Using the dataloaders, train your network. After each epoch, print out the loss (a scalar) and accuracy (a percentage) for both the training and testing datasets. Don't forget your model, data, and labels all need to be moved to the GPU to speed up training (for your model, you need only do this once - for the data, it's for each batch loaded from the dataloader).

<div style="background-color: #d4edda; border-left: 6px solid #28a745; padding: 15px; color: #155724;">
  <strong>🟢 AI Policy: GREEN</strong> <br>
  Generative AI is allowed/encouraged for this section.
</div>

## Improvement

Your goal is to build the best possible classifier (in terms of test accuracy) for this data. You have several hyperparameters you can explore to make this happen.

- You probably noted that your datapoints are quite unregular - some are big, and others are small. Networks *can* learn their way out of this, but they do better if you don't ask them to. You can integrate a `StandardScalar` into your Dataset class to scale the data prior to feeding it into the network. This should act a bit like the OneHotEncoder, where it `fit_transform`s to the training set, but only `transform`s the testing set.
- `SimpleScalar` will normalize data before the first layer. "Batch Normalization" will do the same for intermediate layers (which can be helpful in deeper networks). `model.train()` for training and `model.eval()` for testing are important if you use this.
- Network depth
- Network width
- Activation functions
- Batch size
- Learning rate
- Class weights in the `CrossEntropyLoss` to balance unbalanced classes

We only need to see your best version, but you should tell us about everything else you tried, whether it worked or not.

`~/bin/submit -c=SD312 -p=lab07_classification 07Classification.ipynb` (or whatever you called your .ipynb)