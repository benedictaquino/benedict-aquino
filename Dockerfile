# Use an official Python runtime as a parent image
FROM continuumio/miniconda3

# Set the working directory to /website
WORKDIR /website

# Copy the current directory contents into the container at /website
COPY . /website

# Set up conda environment
RUN conda env create -f website.yml
RUN echo "source activate website" > ~/.bashrc
ENV PATH /opt/conda/envs/website/bin:$PATH

# Make port 80 available to the world outside this container
EXPOSE 8000

# Run app.py when the container launches
CMD ["python", "app/app.py"]
