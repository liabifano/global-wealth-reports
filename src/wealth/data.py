PREFIX_PATH = 'https://www.credit-suisse.com/media/assets/corporate/docs/about-us/research/publications/global-wealth-databook-{}.pdf'
YEARS = [2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011, 2010]

PATHS = [PREFIX_PATH.format(x) for x in YEARS]



if __name__=='__main__':
    for x in PATHS:
        print(x)
