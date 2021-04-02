# Visualizations Landing
This repository contains the landing page for https://nocovid.group. 
### Deployment
Deployment is done automatically via the [CICD pipeline](https://github.com/aochen-jli/visualizations-cicd), 
available for monitoring at https://concourse.nocovid.group. The displayed regions are set upon deployment. 
### Integration
Integration with visualizations requires additional values to be added to the `regions` section of the 
[visualizations app](https://github.com/aochen-jli/visualizations) values.yaml file. Documentation is available in 
that repo. Additionally, when a deployment pipeline is created for a new rankings repository, the landing deployment
pipeline must be modified accordingly to read from that repo's values.yaml file.
