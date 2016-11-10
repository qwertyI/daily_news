how to deploy a jenkins job?

1.click new_item button

![new_item](https://bytebucket.org/percolata/qa/raw/e8b461c88cda969a9f697e5fbf89f5699553319a/safe/new_item.png?token=851dd00bead9a2d1d19d9a529562168aad677be0)

2.enter your job name and select freestyle job

![new_job](https://bytebucket.org/percolata/qa/raw/e8b461c88cda969a9f697e5fbf89f5699553319a/safe/new_job.png?token=5feb298f4f2de0f21433f69bc999972e87f0cdee)

3.set Discard Old Builds and where the project can be run

![basic_set](https://bytebucket.org/percolata/qa/raw/e8b461c88cda969a9f697e5fbf89f5699553319a/safe/basic_set.png?token=713ff47fac73b8ff103c95538e53c4796b20d3d8)

4.if we need run autotest case when we push the code to git, we can set source code management.

![git_set](https://bytebucket.org/percolata/qa/raw/e8b461c88cda969a9f697e5fbf89f5699553319a/safe/git_set.png?token=e49ea323f4bfcaeb1a7179fd0ee8ad468aeab4d9)

more attention is we should add hook permission in git or bitbucket before we set it!

5.set build trigger

![trigger](https://bytebucket.org/percolata/qa/raw/7c0fdefc385e1e7e48527e09f21aa74d5ca74dff/safe/build_trigger.png?token=4428008b74aefcf30d68da06247e64e939864529)

set Build periodically: H 1 * * * .will run the job every 1 AM UTC, more info we can click '?' on the right!And if we set source code managerment in step 4, we also should select 'Build when a changes is pushed to BitBucket' to make it work!

6.build command

![build_selection](https://bytebucket.org/percolata/qa/raw/7c0fdefc385e1e7e48527e09f21aa74d5ca74dff/safe/build_selection.png?token=93a6b276dcab06674d27bb443d66eb06f974730f)

![build_command](https://bytebucket.org/percolata/qa/raw/7c0fdefc385e1e7e48527e09f21aa74d5ca74dff/safe/build_command.png?token=706796ca22d007a36cfcda156af317c4fe007992)

we can select Execute Windows batch command or Execute shell then enter command!

7.Save the job.

