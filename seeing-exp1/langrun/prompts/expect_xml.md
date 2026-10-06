After the file, also write what should happen as an ```expect block, one expectation per line, in these forms:

```expect
ball touches ramp
ball comes to rest in cup
ball drops through hoop
door reaches its lower stop
```

A name is a body or geom name from your file (`bucket` also covers geoms named `bucket_...`). After each run your
expectations are checked against it and you are told which hold. A ball counts as at rest when it moves slower than
5 cm/s at the end. If you send a corrected file, send its ```expect block again.
