# DVC Implementation for Dataset and Model Tracking

This guide will walk you through the steps to implement Data Version Control (DVC) for tracking datasets and models in FlowMovieML. We will be setting up two remotes, "dataset-track" and "model-track", in Azure.

## Prerequisites

Before we start, make sure you have the following:

- Azure CLI installed
- An Azure account

### Step 1: Install Azure CLI

If you haven't installed the Azure CLI yet, you can do so with the following command:

```bash
brew update && brew install azure-cli
```

### Step 2: Login to Azure

Login to your Azure account with the following command:

```bash
az login
```

### Step 3: Get Azure Storage Connection String

To get the connection string for your Azure Storage account, run the following command:

```bash
az storage account show-connection-string --name <storage_account> --query connectionString --output tsv
export AZURE_STORAGE_CONNECTION_STRING="<connection_string>"
```

Replace `<storage_account>` with the name of your Azure Storage account. This connection string will be 
used to set up the remotes in DVC.

### Step 4: DVC Setup

Now that we have the connection string, we can set up the remotes in DVC. First, initialize DVC in your project:

```bash
dvc init
```

Next, add the remotes for dataset and model tracking:

```bash
dvc remote add dataset-track azure://<container_name>/dataset
dvc remote add models-track azure://<container_name>/models
```

Replace `<container_name>` with the name of the container in your Azure Storage account where you want to store the datasets and models.

### Step 5: Add Data

To push data to the remotes, you can use the following commands:

```bash
dvc add dataset/financials.csv
dvc add dataset/movies.csv
dvc add dataset/opening_gross.csv

dvc add models/models.pkl
dvc add models/scaler.pkl
```

This will create `.dvc` files for each dataset and model, which you can then push to the remotes:

```bash
dvc push dataset/financials.csv -r dataset-track
dvc push dataset/movies.csv -r dataset-track
dvc push dataset/opening_gross.csv -r dataset-track
```



