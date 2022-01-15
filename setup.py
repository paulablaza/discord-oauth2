import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
  name='discord-oauth2',                           
  packages=setuptools.find_packages(),                  
  version='0.2',                              
  license='MIT',                              
  description="A python library that uses discord's api for easy authentication for your website.",
  long_description=long_description,              
  long_description_content_type="text/markdown",  
  author='Paul Martin Ablaza',
  author_email='ablazapaulmartin@protonail.com',
  url='https://github.com/paulablaza/discord-oauth2', 
  install_requires=['requests'], 
  keywords=["discord auth", "discord oauht2", "oauth2"], 
  classifiers=[                                   
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',

        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ]
)