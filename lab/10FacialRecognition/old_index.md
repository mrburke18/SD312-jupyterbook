---
title: Facial Recognition
---

In this lab, you will build a facial recognition system. Like other large-scale neural net projects, the creation and training of an embedding system for faces that would work impressively on real images is probably beyond the scope of our available time and expense.  However, we can certainly use some pre-trained networks, and build a facial recognition system from them. In this lab, DO NOT USE THE GPU... it will run out of memory and there is no need as we are not training any models, we are using existing models with our own datasets.

A facial recognition system normally consists of two networks, one which *detects* faces, and the other which *embeds* faces.  We'll be using the open-source project facenet to do this.

[Here's your notebook](10FacialRecognition.ipynb).

**Installing a pre-trained network**

Pytorch doesn't have a pre-trained network for facial recognition, so we'll be using a github repo with pre-trained weights.

- In your AWS JupyterLab, open a Terminal.
- run `cd SageMaker`
- run `git clone https://github.com/timesler/facenet-pytorch.git facenet_pytorch`
- If unable I have downloaded it [here](./facenet_pytorch)

**Getting MIDN Portraits**
For now I will provide a small dataset for you to work with. With the complete class available in next day

**Opening an image**

If the image is available locally, this can look like this:

```python
from PIL import Image
img = Image.open('path/to/image.jpg')
img.load()
```


**Displaying an image**

If it's a PIL Image or numpy array, you can do this with

```python
import matplotlib.pyplot as plt
plt.imshow(img)
```

If it's a torch tensor, it keeps RGB in a different order, so you need to do this:

```python
import matplotlib.pyplot as plt
plt.imshow(img.permute(1,2,0))
```

**Cropping an image using a face detector**

Assume `img` is a PIL Image.

```python
from facenet_pytorch import MTCNN
mtcnn = MTCNN(keep_all=True)
#You can take out the keep_all parameter if you only want one face from each image
mtcnn.eval()
cropped_img = mtcnn(img)
```

**Building an embedding of a cropped face**

Assume `cropped_img` is a tightly-cropped picture of a face.

```python
from facenet_pytorch import InceptionResnetV1
resnet = InceptionResnetV1(pretrained='vggface2')
resnet.eval()
embedding = resnet(img_cropped)
```

**Everyone taking SI470**

There is a portion of the lab which requires you to collect the images of all members of SI470.  We might expand this to instead be your CS cohort. [prelimenary_data](./prelimenary_data) 



**What you should know after doing this lab (aside from the coding part)**

- Images should be cropped before being embedded.
- The process of building a facial recognition system: embed the gallery images, embed the probe image, find the closest gallery embeddings to the probe embedding.
