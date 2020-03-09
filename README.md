
Setup a function to wrap aws-azure-login

```
aws-azure-login(){ profile=$1 ; shift ; $(which aws-azure-login) --profile=$profile $* ; }
```

Copy this script to someone fixed

```
cp aws-azure-login-complete-bash.py ~/.bash_completion.d/
```

Set this script to complete

```
complete -C ~/.bash_completion.d/aws-azure-login-complete-bash.py aws-azure-login
```

Issues
===

The wrapper function is quite dumb so you need to specify the profile first e.g.
```
aws-azure-login lse-cpec-stride-prod --mode debug
```
and not
```
aws-azure-login --mode debug lse-cpec-stride-prod
```
