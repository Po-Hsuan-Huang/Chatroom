

## Downloading LLaMA 3 Model

### Download

To download the model weights and tokenizer, please visit the Meta Llama website and accept our License.

Once your request is approved, you will receive a signed URL over email. Then, run the `download.sh` script, passing the URL provided when prompted to start the download.

### Pre-requisites

Ensure you have `wget` installed. Then run the script:

```bash
./download.sh
```

Remember that the links expire after 24 hours and a certain amount of downloads. You can always re-request a link if you start seeing errors such as `403: Forbidden`.

### Access to Hugging Face

We also provide downloads on Hugging Face, in both transformers and native llama3 formats. To download the weights from Hugging Face, please follow these steps:

1. Visit one of the repos, for example [meta-llama/Meta-Llama-3.1-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3.1-8B-Instruct).
2. Read and accept the license. Once your request is approved, you'll be granted access to all Llama 3.1 models as well as previous versions. Note that requests used to take up to one hour to get processed.
3. To download the original native weights to use with this repo, click on the "Files and versions" tab and download the contents of the original folder. You can also download them from the command line if you `pip install huggingface-hub`:

```bash
huggingface-cli download meta-llama/Meta-Llama-3.1-8B-Instruct --include "original/*" --local-dir meta-llama/Meta-Llama-3.1-8B-Instruct
```

**NOTE**: The original native weights of `meta-llama/Meta-Llama-3.1-405B` would not be available through this Hugging Face repo.
