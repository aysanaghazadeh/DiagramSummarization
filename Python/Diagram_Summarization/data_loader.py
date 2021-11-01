import os
import torch
import torchvision
import pandas as pd

def Load_Summaries(directory):
    submission = pd.read_csv(directory)
    cols = ['Answer.summary', 'Input.image_url']
    summaries = submission[['summary', 'filename']]
    return summaries

def Load_Data(directory):
    summary_directory = '/Users/aysanaghazadeh/University/Pitt/Research/Diagram_Summarization/ai2d-rst-v1-1/Summaries/summaries.csv'
    summaries = Load_Summaries(summary_directory)
    data_dir = directory
    filenames = [name for name in os.listdir(data_dir)]
    batch_size = len(list(summaries['filename']))
    batch = torch.zeros(batch_size, 3, 1500, 1500, dtype=torch.uint8)
    files = []
    summary = []
    transform = torchvision.transforms.Compose([torchvision.transforms.Resize(255),
                                    torchvision.transforms.CenterCrop(224),
                                    torchvision.transforms.ToTensor()
                                    ])
    count = 0
    for i, filename in enumerate(filenames):
        if filename in list(summaries['filename']):
            image = torchvision.io.read_image(os.path.join(data_dir, filename))
            image = torchvision.transforms.functional.pad(image, get_padding(image))
            batch[i - count] = image
            files.append(filename)
            summary.append(summaries['summary'][i - count])
        else:
            count += 1

    return batch, filename, summary


def get_padding(image):
    max_w = 1500
    max_h = 1500
    imsize = image.shape
    h_padding = (max_w - imsize[2]) / 2
    v_padding = (max_h - imsize[1]) / 2
    l_pad = h_padding if h_padding % 1 == 0 else h_padding + 0.5
    t_pad = v_padding if v_padding % 1 == 0 else v_padding + 0.5
    r_pad = h_padding if h_padding % 1 == 0 else h_padding - 0.5
    b_pad = v_padding if v_padding % 1 == 0 else v_padding - 0.5

    padding = (int(l_pad), int(t_pad), int(r_pad), int(b_pad))

    return padding

# image_directory = '/Users/aysanaghazadeh/University/Pitt/Research/Diagram_Summarization/ai2d-rst-v1-1/images'
# images, filenames, summary = Load_Data(image_directory)



