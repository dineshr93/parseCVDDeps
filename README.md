
cuttlefish The generated file is built under: out/host/linux-x86/cvd-host_package.tar.gz

The file is too large (511.12MB).
Opening it might take some time and might make the IDE unresponsive. Do you want to open 'out/host/linux-x86/cvd-host_package.tar.gz' anyway?

```
entry point: device/google/cuttlefish/build/Android.bp
registry file: out/target/product/skilfish_car_cf/module-info.json


./aospparse-amd64 ../device/google/cuttlefish/build/Android.bp cvd_host_tools >deps.txt
./aospparse-amd64 ../device/google/cuttlefish/build/Android.bp cvd_openwrt_images >>deps.txt
./aospparse-amd64 ../device/google/cuttlefish/build/Android.bp cvd_host_model_simulator_files >>deps.txt
./aospparse-amd64 ../device/google/cuttlefish/build/Android.bp cvd_host_acloud_data >>deps.txt
./aospparse-amd64 ../device/google/cuttlefish/build/Android.bp cvd_host_seccomp_policy_x86_64 >>deps.txt
./aospparse-amd64 ../device/google/cuttlefish/build/Android.bp cvd_host_seccomp_policy_aarch64 >>deps.txt
./aospparse-amd64 ../device/google/cuttlefish/build/Android.bp cvd_host_netsim_gui_assets >>deps.txt

python3 process_module_info.py ../out/target/product/skilfish_car_cf/module-info.json --deps-file deps.txt --all-depsclasses
python3 process_module_info.py ../out/target/product/skilfish_car_cf/module-info.json --deps-file deps.txt
python3 process_module_info.py ../out/target/product/skilfish_car_cf/module-info.json --all-classes
python3 process_module_info.py ../out/target/product/skilfish_car_cf/module-info.json --module-key=webrtc_operator


```

misc:

Soong deps registry (common for both) only cc files and no header files
out/soong/module_bp_cc_deps.json
out/soong/mmodule_bp_java_deps.json

PAth info (potential registry to find and gather source code)
/home/aosp/foss/out/target/product/skilfish_car_cf/module-info.json

jq '.["cvd-host_package"]' module-info.json


./aospparse-amd64 ../device/google/cuttlefish/build/Android.bp cvd_openwrt_images >>deps.txt
dira271641@deulm2ts016:/home/aosp/out/host/linux-x86/etc/openwrt/images$ ls -lh
total 25M
-rw-r--r-- 1 dira271641 root  10M Jun  9 02:29 openwrt_kernel_aarch64
-rw-r--r-- 1 dira271641 root 5.0M Jun  9 02:29 openwrt_kernel_x86_64
-rw-r--r-- 1 dira271641 root 132M Jun  9 02:34 openwrt_rootfs_aarch64
-rw-r--r-- 1 dira271641 root 133M Jun  9 02:34 openwrt_rootfs_x86_64
