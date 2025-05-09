import torch

def main():
    print(torch.__version__)
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    print( torch.cuda.is_available() )
if __name__ == '__main__':
    main()