# Programming Connected Devices practical work repository

This repository contains the description of the labs for the Programming Connected Devices course of EMSE ICM M-INFO, M1 CPS2, M2 CPS2.

## Order of the labs

1. [`lab_testing_electronic_components.adoc`](lab_testing_electronic_components.adoc)
2. [`lab_esp32_micropython_intro.adoc`](lab_esp32_micropython_intro.adoc)
3. [`lab_esp32_micropython_project.adoc`](lab_esp32_micropython_project.adoc)
4. ... more soon ...


## How to use this project

The first thing you need to do is to clone your project, and merge this branch into your repository.

Assume your group is #1

```
group=1
```

1. clone your project

```
git clone git@gitlab.emse.fr:isi/enseignements/m-info/iot/groups/$group.git
```

or if you haven't yet added a SSH key for secure access to GitLab (link:https://gitlab.emse.fr/help/user/ssh.md[learn more]):

```
git clone https://gitlab.emse.fr/isi/enseignements/m-info/iot/groups/$group.git
```

2. add this project as the `labs` remote, and fetch it.

```
git remote add labs git@gitlab.emse.fr:cps2/pcd/labs.git
git fetch labs
```

or 

```
git remote add labs https://gitlab.emse.fr/cps2/pcd/labs.git
git fetch labs
```

3. merge `labs/master` into your `master` branch

```
git merge labs/master
```

Now your `master` branch is in sync with this version. You can directly edit the **adoc** documents, commit with informative messages, and push your changes. 
