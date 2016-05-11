# ToupCam API Manual

* * *

# <font color="#0000FF">1\. Version</font>

* * *

> 1.1.4615.20141230

* * *

# <font color="#0000FF">2\. Introduction</font>

* * *

ToupCam cameras (model series: UCMOS, WCMOS, LCMOS, U3CMOS, L3CMOS, ICMOS, GCMOS, UHCCD, EXCCD, SCCCD) support various kinds of APIs (Application Program Interface), namely Native C/C++, .NET/C#/VB.NET, [DirectShow](http://msdn.microsoft.com/en-us/library/windows/desktop/dd375454(v=vs.85).aspx), [Twain](http://twain.org/), LabView and so on. Compared with other APIs, Native C/C++ API, as a low level API, don't depend any other runtime libraries. Besides, this interface is simple, flexible and easy to be integrated into the customized applications. The SDK zip file contains all of the necessary resources and information:

*   inc

> toupcam.h, C/C++ head file  
> toupcam.cs, for C#. The toupcam.cs use P/Invoke to call into toupcam.dll. Please copy toupcam.cs to your C# project to use it.  
> toupcam.vb, for VB.NET. The toupcam.vb use P/Invoke to call into toupcam.dll. Please copy toupcam.vb to your VB.NET project to use it.

*   win: For Microsoft Windows
    *   x86

    > toupcam.lib, lib file for x86.  
    > toupcam.dll, dll file for x86.  
    > toupcamdemocpp.exe, x86 C++ demo exe file.

    *   x64

    > toupcam.lib, lib file for x64.  
    > toupcam.dll, dll file for x64.  
    > toupcamdemocpp.exe, x64 C++ demo exe file.

    *   drivers

        > x86 folder contains the kernel mode drivers for x86, including toupcam.cat, toupcam.inf and toupcam.sys.  
        > x64 folder contains the kennel mode driver for x64, including toupcam.cat, toupcam.inf and toupcam.sys.

    *   samples

        > a). toupcamdemocpp, C++ sample. It demonstrates to enumerate device, open device, video preview, image capture, set the preview resolution, multi-format image saving (.bmp, .jpg, .png, etc), wmv format video recording and so on. This sample use Pull Mode. To keep the code clean, this sample uses the WTL library which can be downloaded from [http://sourceforge.net/projects/wtl](http://sourceforge.net/projects/wtl/)
        > 
        > b). toupcamdemomfc, a simple C++ sample. It use MFC as the GUI library. It demonstrates to open device, video preview, image capture, set the preview resolution, multi-format image saving (.bmp, .jpg, .png, etc). This sample use Pull Mode.
        > 
        > c). toupcamdemowinformcs1, C# winform sample. This sample use Pull Mode, StartPullModeWithWndMsg.
        > 
        > d). toupcamdemowinformcs2, C# winform sample. This sample use Pull Mode, StartPullModeWithCallback.
        > 
        > e). toupcamdemowinformvb, VB.NET winform sample. This sample use Pull Mode.

    *   extras

        > a). directshow directory contains the DirectShow SDK and demo.  
        > b). twain directory contains the TWAIN SDK and demo.  
        > c). labview directory contains the Labview SDK and demo.

*   linux: For Linux.

*   osx: For MAC OSX.

*   doc: User manuals in English and Chinese.

* * *

# <font color="#0000FF">3\. Modes for accessing image data: "Pull Mode" vs "Push Mode"</font>

* * *

Toupcam offers two modes to obtain image data: Pull Mode and Push Mode. The former is recommended since it's simpler and the application seldom gets stuck in multithreading conditions, especially when using windows message to notify the events.

*   In Pull Mode, toupcam plays a passive role and the application 'PULL' image data from toupcam. The internal thread of toupcam obtains image data from the camera hardware and saves them to the internal buffers, then notify the application (see below). The application then call functions Toupcam_PullImage and Toupcam_PullStillImage to access image data.

> There are to ways to notify applications:

1.  Use Windows message: Start pull mode by using the function Toupcam_StartPullModeWithWndMsg. When event occurs, toupcam will post message (PostMessage) to the specified window. Parameter WPARAM is the event type, refer to the definition of TOUPCAM_EVENT_xxxx. This model avoids the multithreading issues, so it's the most simple way. ( <span id="ouHighlight__0_1TO0_8" abp="328" paragraphname="paragraph0" srcinfo="0:1" dstinfo="0:8">Obviously</span><span id="noHighlight_0.3604163754541626" abp="329">,</span> <span id="noHighlight_0.4641191291796428" abp="330"></span> <span id="ouHighlight__3_4TO11_14" abp="331" paragraphname="paragraph0" srcinfo="3:4" dstinfo="11:14">this</span> <span id="noHighlight_0.02012400177838297" abp="332">is</span> <span id="ouHighlight__7_7TO16_19" abp="333" paragraphname="paragraph0" srcinfo="7:7" dstinfo="16:19">only</span> <span id="noHighlight_0.2751875034297989" abp="334"></span> <span id="ouHighlight__8_9TO21_28" abp="335" paragraphname="paragraph0" srcinfo="8:9" dstinfo="21:28">supported</span> <span id="noHighlight_0.3400843924475497" abp="336">in</span> <span id="ouHighlight__10_16TO30_37" abp="337" paragraphname="paragraph0" srcinfo="10:16" dstinfo="30:37">Windows</span> <span id="ouHighlight__17_18TO38_44" abp="338" paragraphname="paragraph0" srcinfo="17:18" dstinfo="38:44">systems</span><span id="noHighlight_0.38054847537407715" abp="339">,</span> <span id="noHighlight_0.5308658947211726" abp="340"></span> <span id="ouHighlight__23_27TO47_52" abp="341" paragraphname="paragraph0" srcinfo="23:27" dstinfo="47:52">and not supported in Linux</span> <span id="ouHighlight__28_28TO53_55" abp="342" paragraphname="paragraph0" srcinfo="28:28" dstinfo="53:55">and</span> <span id="noHighlight_0.7539774307626169" abp="343"></span> <span id="ouHighlight__29_33TO57_62" abp="344" paragraphname="paragraph0" srcinfo="29:33" dstinfo="57:62">MacOS</span><span id="noHighlight_0.3230648083041762" abp="349">.</span>)
2.  Use Callback function: Start pull mode by using the function Toupcam_StartPullModeWithCallback. When event occurs, toupcam will callback the function PTOUPCAM_EVENT_CALLBACK.

> In Pull Mode, the SDK could not only notify the application that the image data or still image are available for 'PULL', but also inform you of the other events, such as:

<div align="center">

<table width="80%" border="1" cellpadding="0" cellspacing="0" bgcolor="#B0D0B0">

<tbody>

<tr>

<td width="27%" valign="top">TOUPCAM_EVENT_EXPOSURE</td>

<td width="73%" valign="top">exposure time changes</td>

</tr>

<tr>

<td width="27%" valign="top">TOUPCAM_EVENT_TEMPTINT</td>

<td width="73%" valign="top">white balance parameters changes</td>

</tr>

<tr>

<td width="27%" valign="top">TOUPCAM_EVENT_IMAGE</td>

<td width="73%" valign="top">Video image data arrives. Use Toupcam_PullImage to 'pull' the image data</td>

</tr>

<tr>

<td width="27%" valign="top">TOUPCAM_EVENT_STILLIMAGE</td>

<td width="73%" valign="top">Still image which is triggered by function Toupcam_Snap arrives. Use Toupcam_PullStillImage to 'pull' the image data</td>

</tr>

<tr>

<td width="27%" valign="top">TOUPCAM_EVENT_ERROR</td>

<td width="73%" valign="top">Error occurs, data acquisition cannot continue</td>

</tr>

<tr>

<td width="27%" valign="top">TOUPCAM_EVENT_DISCONNECTED</td>

<td width="73%" valign="top">Camera disconnected, maybe has been pulled out</td>

</tr>

</tbody>

</table>

</div>

*   In Push Mode, toupcam plays an active role. Once the video data is obtained from camera by internal thread, toupcam will 'PUSH' the image data to the application through PTOUPCAM_DATA_CALLBACK. Call the function Toupcam_StartPushMode to start push mode. Push mode is more complex. There are some special precautions, such as multithread issues, being impossible to call Toupcam_Close and Toupcam_Stop in callback function PTOUPCAM_DATA_CALLBACK, etc.

* * *

# <font color="#0000FF">4\. Functions</font>

* * *

*   ## Toupcam_Enum

> Return Value: non-negative integer, enumerated camera number
> 
> Parameters: ToupcamInst buffer
> 
> Remarks:
> 
> > call this function to enumerate ToupCam cameras that are currently connected to computer and when it is returned, ToupcamInst buffer contains the information of each camera instance enumerated.**If we don't care about that multiple cameras connect to the computer simultaneously, it's optional to call this function to enumerate the camera instances**.
> > 
> > The code snippet shows as below:  
> > 
> > <table width="100%" border="0" bgcolor="#B0D0B0">
> > 
> > <tbody>
> > 
> > <tr>
> > 
> > <td>ToupcamInst arr[TOUPCAM_MAX];  
> > unsigned cnt = Toupcam_Enum(arr);  
> > for (unsigned i = 0; i < cnt; ++i)  
> >     ......</td>
> > 
> > </tr>
> > 
> > </tbody>
> > 
> > </table>
> > 
> > <table width="100%" border="0" bgcolor="#B0D0B0">
> > 
> > <tbody>
> > 
> > <tr>
> > 
> > <td>typedef struct{  
> >  #ifdef _WIN32  
> >    const wchar_t*  name; /* model name */  
> >  #else  
> >    const char*    name;  
> >  #endif  
> >    unsigned     flag; /* TOUPCAM_FLAG_xxx */  
> >    unsigned     maxspeed; /* number of speed level, Toupcam_get_MaxSpeed, the speed range = [0, max], closed interval */  
> >    unsigned     preview; /* number of preview resolution, Toupcam_get_ResolutionNumber */  
> >    unsigned     still; /* number of still resolution, Toupcam_get_StillResolutionNumber */  
> >    ToupcamResolution  res[TOUPCAM_MAX];  
> > }ToupcamModel;</td>
> > 
> > </tr>
> > 
> > </tbody>
> > 
> > </table>

*   ## Toupcam_Open

Return Value: HToupCam handle. Return NULL when fails (Such as the device has been pulled out).

Parameters: ToupCam camera instance, enumerated by Toupcam_Enum. **If id is NULL, Toupcam_Open will open the first camera which connects to the computer. So, if we don't care about that multiple cameras connect to the computer simultaneously, Toupcam_Enum is optional, we can simply use NULL as the parameter.**

Remarks: open the camera instance.

*   ## Toupcam_HotPlug

Return Value: NA

Parameters:

> PTOUPCAM_HOTPLUG pHotPlugCallback: callback function
> 
> > <table width="100%" border="0" bgcolor="#B0D0B0">
> > 
> > <tbody>
> > 
> > <tr>
> > 
> > <td>
> > 
> > <div align="center">typedef void (*PTOUPCAM_HOTPLUG)(void* pCallbackCtx);</div>
> > 
> > </td>
> > 
> > </tr>
> > 
> > </tbody>
> > 
> > </table>
> 
> void* pCallbackCtx: callback context

Remarks:

> This function only exists on OSX and Linux, it's unnecessary on Windows.
> 
> To process the device plug in / pull out in Windows, please refer to the MSDN([Device Management](http://msdn.microsoft.com/en-us/library/windows/desktop/aa363224(v=vs.85).aspx), [Detecting Media Insertion or Removal](http://msdn.microsoft.com/en-us/library/windows/desktop/aa363215(v=vs.85).aspx)).
> 
> To process the device plug in / pull out in Linux / OSX, please call this function to register the callback function. When the device is inserted or pulled out, you will be notified by the callback funcion, and then call Toupcam_Enum(...) again to enum the cameras.

*   ## Toupcam_Close

    Return Value: void

    Parameters: HToupCam handle

    Remarks: close the camera instance. After it is closed, never use the HToupCam handle any more. **Do not call Toupcam_Close in the PTOUPCAM_EVENT_CALLBACK and PTOUPCAM_DATA_CALLBACK callback function, otherwise, deadlock occurs.**

*   ## Toupcam_StartPullModeWithWndMsg and Toupcam_StartPullModeWithCallback

    Return Value: HRESULT type means "success/ failure"

    Parameters:

    *   HToupCam h: instance handle opened by Toupcam_Open
    *   HWND hWnd: event occurs, message will be posted in this window
    *   UINT nMsg: Windows custom message type. Its WPARAM parameter means event type TOUPCAM_EVENT_xxxx, LPARAM is useless (always zero)
    *   PTOUPCAM_EVENT_CALLBACK pEventCallback, void* pCallbackContext: callback function specified by user's application and callback context parameter. This callback function is called back from the internal thread in toupcam.dll, so great attention should be paid to multithread issue. Do not call Toupcam_Stop and Toupcam_Close in this callback function, otherwise, deadlock occurs.

    > <table width="100%" border="0">
    > 
    > <tbody>
    > 
    > <tr>
    > 
    > <td bgcolor="#B0D0B0">
    > 
    > <div align="center">typedef void (__stdcall* PTOUPCAM_EVENT_CALLBACK)(unsigned nEvent, void* pCallbackCtx);</div>
    > 
    > </td>
    > 
    > </tr>
    > 
    > </tbody>
    > 
    > </table>

    Remarks: Obviously, Toupcam_StartPullModeWithWndMsg is only supported in Windows OS.

*   ## Toupcam_PullImage and Toupcam_PullStillImage

    Return Value: HRESULT type means "success/ failure"

    Parameters:

*   HToupCam h: instance handle opened by Toupcam_Open
*   void* pImageData: Data buffer. Users have to make sure that the data buffer capacity is enough to save the image data.
*   int bits: 24, 32 or 8, means RGB24, RGB32 or 8 bits grey images. This parameter is ignored in RAW mode.
*   unsigned* pnWidth, unsigned* pnHeight: width and height of image.

> Remarks: when pImageData is NULL, while pnWidth and pnHeight are not NULL, you can peek the width and height of images.

*   ## Toupcam_StartPushMode

    Return Value: HRESULT type means "success / failure"

    Parameters:

    *   HToupCam h: instance handle opened by Toupcam.
    *   Open PTOUPCAM_DATA_CALLBACK pDataCallback, void* pCallbackCtx: the callback function and callback context parameters that are specified by the user's program. Toupcam.dll gets image data from the camera, then calls back this function.

> <table width="100%" border="0" bgcolor="#B0D0B0">
> 
> <tbody>
> 
> <tr>
> 
> <td>
> 
> <div align="center">typedef void (*PTOUPCAM_DATA_CALLBACK)(const void* pData, const BITMAPINFOHEADER* pHeader, BOOL bSnap, void* pCallbackCtx);</div>
> 
> </td>
> 
> </tr>
> 
> </tbody>
> 
> </table>

> when calls back, if Parameter pData == NULL, then internal error occurs (eg: the camera pulled out suddenly).  
> For parameter BOOL bSnap, TRUE means still image snap by Toupcam_Snap function, FALSE means ordinary previewed pictures/ videos.  
> Attention: this callback function is called back from the internal thread in toupcam.dll, so great attention should be paid to multithread issue. Do not call Toupcam_Stop and Toupcam_Close in this callback function, otherwise, deadlock occurs.

> Remarks: start camera instance.

*   ## Toupcam_Stop

    Return Value: HRESULT type means success/failure

    Parameters: HToupCam handle

    Remarks: stop the camera instance. Do not call Toupcam_Stop in the PTOUPCAM_EVENT_CALLBACK and PTOUPCAM_DATA_CALLBACK callback function, otherwise, deadlock occurs. After stopped, it can be restart again. For example, switching the video resolution:

    *   Step 1: call Toupcam_Stop to stop
    *   Step 2: call Toupcam_put_Size or Toupcam_put_eSize to set the new resolution
    *   Step 3: call Toupcam_Startxxxx to restart
*   ## Toupcam_Pause

    Return Value: HRESULT type means success/failure

    Parameters: HToupCam handle

    Remarks: pause/continue camera instance.

*   ## Toupcam_Snap

> Return Value: HRESULT type means success/failure
> 
> Parameters:

*   HToupCam h: camera instance handle
*   ULONG nResolutionIndex: resolution index wanted.

> Remarks: snap 'still' image. When snap successfully:
> 
> > a) If we use Pull Mode, it will be notified by TOUPCAM_EVENT_STILLIMAGE.
> > 
> > b) If we use Push Mode, the image will be returned by callback function PTOUPCAM_DATA_CALLBACK with the parameter BOOL bSnap is TRUE.

Most cameras can snap still image with different resolutions under continuous preview. For example, UCMOS03100KPA's previewed resolution is 1024*768, if we call Toupcam_Snap(h, 0), we get so called "still image" with 2048*1536 resolution.  
Some cameras hasn't this ability, so nResolutionIndex must be equal the preview resolution which is set by Toupcam_put_Size, or Toupcam_put_eSize.  
Whether it supports "still snap" or not, see "still" domain in ToupcamModel.

*   ## Toupcam_put_Size, Toupcam_get_Size, Toupcam_put_eSize, Toupcam_get_eSize

    Return Value: HRESULT type means success/failure

    Parameters:

    *   HToupCam h: camera instance handle
    *   ULONG nResolutionIndex: current/present resolution index
    *   LONG nWidth, LONG nHeight: width and height of current resolution index

> Remarks: set/get current resolution

> Set resolution before running ToupCam_Startxxxx  
> There are two ways to set current resolution: one is by resolution index, the other by width/height. Both ways are equivalent. For example, UCMOS03100KPA supports the following three kinds of resolution:  
>     Index 0: 2048, 1536  
>     Index 1: 1024, 768  
>     Index 2: 680, 510  
> So Toupcam_put_Size(h, 1024, 768) is as effective as Toupcam_put_eSize(h, 1)

*   ## Toupcam_get_ResolutionNumber, Toupcam_get_Resolution

    Return Value: HRESULT type means success/failure

    Parameters:

    *   HToupCam h: camera instance handle
    *   ULONG nIndex: resolution index
    *   LONG* pWidth, LONG* pHeight: width/height

    Remarks: Toupcam_get_ResolutionNumber means the number of resolution supported. Take UCMOS03100KPA as an example, if we call the function Toupcam_get_ResolutionNumber and get "3", which means it can support three kinds of resolution. Toupcam_get_Resolution obtains the width/height of each kind of resolution.

> These parameters have also been contained in ToupcamModel.

*   ## Toupcam_get_RawFormat

    Return Value: HRESULT type means success/failure

    Parameters:

> HToupCam h: camera instance handle
> 
> unsigned* nFourCC: raw format, see the table
> 
> unsigned* bitts: Bits Count, such as 8, 12, 14, 16
> 
> <div align="center">
> 
> <table width="60%" border="1" cellpadding="0" cellspacing="0" bgcolor="#B0D0B0">
> 
> <tbody>
> 
> <tr>
> 
> <td width="40%" valign="top">MAKEFOURCC('G', 'B', 'R', 'G')</td>
> 
> <td width="60%" valign="top">GBGBGB...  
> RGRGRG...  
> GBGBGB...  
> RGRGRG...  
> ...  
> </td>
> 
> </tr>
> 
> <tr>
> 
> <td width="40%" valign="top">MAKEFOURCC('R', 'G', 'G', 'B')</td>
> 
> <td width="60%" valign="top">RGRGRG...  
> GBGBGB...  
> RGRGRG...  
> GBGBGB...  
> ...  
> </td>
> 
> </tr>
> 
> <tr>
> 
> <td width="40%" valign="top">MAKEFOURCC('B', 'G', 'B', 'R')</td>
> 
> <td width="60%" valign="top">BGBGBG...  
> BRBRBR...  
> BGBGBG...  
> BRBRBR...  
> ...  
> </td>
> 
> </tr>
> 
> <tr>
> 
> <td width="40%" valign="top">MAKEFOURCC('G', 'R', 'B', 'G')</td>
> 
> <td width="60%" valign="top">GRGRGR...  
> BGBGBG...  
> GRGRGR...  
> BGBGBG...  
> ...  
> </td>
> 
> </tr>
> 
> <tr>
> 
> <td width="40%" valign="top">MAKEFOURCC('Y', 'V', 'Y', 'U')</td>
> 
> <td width="60%" valign="top">YUV4:2:2, please see: [http://www.fourcc.org](http://www.fourcc.org)</td>
> 
> </tr>
> 
> </tbody>
> 
> </table>
> 
> </div>

*   ## Toupcam_put_Option, Toupcam_get_Option

    Return Value: HRESULT type means success/failure

    Parameters:

> HToupCam h: camera instance handle
> 
> unsigned iOption: Option
> 
> unsigned iValue: see the table
> 
> <div align="center">
> 
> <table width="80%" border="1" cellpadding="0" cellspacing="0" bgcolor="#B0D0B0">
> 
> <tbody>
> 
> <tr>
> 
> <td width="28%" valign="top">TOUPCAM_OPTION_NOFRAME_TIMEOUT</td>
> 
> <td width="72%" valign="top">Report error if cannot grab frame in a certain time.  
> 1 = enable this feature; 0 = disable this feature. default: enable.  
> </td>
> 
> </tr>
> 
> <tr>
> 
> <td width="28%" valign="top">TOUPCAM_OPTION_THREAD_PRIORITY</td>
> 
> <td width="72%" valign="top">set the priority of the internal thread which grab data from the usb device.  
> 0 = THREAD_PRIORITY_NORMAL; 1 = THREAD_PRIORITY_ABOVE_NORMAL; 2 = THREAD_PRIORITY_HIGHEST;  
> default: 0;  
> Please refer to [SetThreadPriority](http://msdn.microsoft.com/en-us/library/windows/desktop/ms686277(v=vs.85).aspx)  
> </td>
> 
> </tr>
> 
> <tr>
> 
> <td width="28%" valign="top">TOUPCAM_OPTION_PROCESSMODE</td>
> 
> <td width="72%" valign="top">0 = better image quality, more cpu usage. this is the default value  
> 1 = lower image quality, less cpu usage.  
> </td>
> 
> </tr>
> 
> <tr>
> 
> <td width="28%" valign="top">TOUPCAM_OPTION_RAW</td>
> 
> <td width="72%" valign="top">The default is 0 which means RGB mode.  
> 1 means RAW mode, read the CMOS or CCD raw data.  
> This value can only be changed BEFORE Toupcam_StartXXX.  
> </td>
> 
> </tr>
> 
> </tbody>
> 
> </table>
> 
> </div>

*   ## Toupcam_put_RealTime, Toupcam_get_RealTime

    Return Value: HRESULT type means success/failure

    Parameters:

    *   HToupCam h: camera instance handle
    *   BOOL bEnable: TRUE or FALSE

    Remarks: If you set RealTime mode as TRUE, then you get shorter frame delay but lower frame rate which damages fluency. The default value is FALSE.

*   ## Toupcam_get_AutoExpoEnable, Toupcam_put_AutoExpoEnable, Toupcam_get_AutoExpoTarget, Toupcam_put_AutoExpoTarget, Toupcam_put_MaxAutoExpoTimeAGain

    Return Value: HRESULT type means success/failure

    Parameters:

    *   HToupCam h: camera instance handle
    *   BOOL bAutoExposure: TRUE or FALSE
    *   USHORT Target: auto-exposure target
    *   ULONG maxTime, USHORT maxAGain: the maximum time and maximum analog gain of auto-exposure

    Remarks: If auto exposure is enabled, the exposure time and analog gain are controlled by software to make the average brightness of the target rectangle as close as possible to the auto exposure target. The auto exposure target value is the target brightness of the target rectangle (see Toupcam_put_AEAuxRect, Toupcam_get_AEAuxRect).

*   ## Toupcam_get_ExpoTime, Toupcam_put_ExpoTime, Toupcam_get_ExpTimeRange

    Return Value: HRESULT type means success/failure

    Parameters:

    *   HToupCam h: camera instance handle
    *   ULONG Time: exposure time, unit: microsecond
    *   ULONG* nMin, ULONG* nMax, ULONG* nDef: the minimum, maximum and default value of exposure time.

> Remarks: exposure time related.

*   ## Toupcam_get_ExpoAGain, Toupcam_put_ExpoAGain, Toupcam_get_ExpoAGainRange

    Return Value: HRESULT type means success/failure

    Parameters:

    *   HToupCam h: camera instance handle
    *   USHORT AGain: analog gain, shown in percentage, eg, 200 means the analog gain is 200%
    *   USHORT* nMin, USHORT* nMax, USHORT* nDef: the minimum, maximum and default value of analog gain.

> Remarks: analog gain related.

*   ## Toupcam_put_Hue, Toupcam_get_Hue, Toupcam_put_Saturation, Toupcam_get_Saturation, Toupcam_put_Brightness, Toupcam_get_Brightness, Toupcam_get_Contrast, Toupcam_put_Contrast, Toupcam_get_Gamma, Toupcam_put_Gamma

    Return Value: HRESULT type means success/failure

    Parameters: HToupCam h: camera instance handle

    Remarks: set or obtain hue, saturation, brightness, contrast and gamma.

*   ## Toupcam_get_Chrome, Toupcam_put_Chrome

    Return Value: HRESULT type means success/failure

    Parameters:

    *   HToupCam h: camera instance handle
    *   BOOL bChrome: TRUE or FALSE

    Remarks: color or gray mode

*   ## Toupcam_get_VFlip, Toupcam_put_VFlip, Toupcam_get_HFlip, Toupcam_put_HFlip

    Return Value: HRESULT type means success/failure

    Parameters: HToupCam h: camera instance handle

    Remarks: vertical/horizontal flip.

*   ## Toupcam_put_Speed, Toupcam_get_Speed, Toupcam_get_MaxSpeed

    Return Value: HRESULT type means success/failure

    Parameters:

    *   HToupCam h: camera instance handle
    *   USHORT nSpeed: frame rate level

    Remarks: the minimum frame rate level is "0", the maximum one can be achieved through Function "Toupcam_get_MaxSpeed" which equals to maxspeed in ToupcamModel.

    Remind: CCD cameras cannot change frame rate setting real-timely, that's to say you can't change the frame rate setting any more after calling the function Toupcam_Startxxxx. Therefore, the frame rate for CCD cameras should be set after function Toupcam_Open but before function Toupcam_Startxxxx.

*   ## Toupcam_put_HZ, Toupcam_get_HZ

    Return Value: HRESULT type means success/failure

    Parameters:

    *   HToupCam h: camera instance handle
    *   int nHZ: 0: 60Hz alternating current, 1: 50Hz alternating current, 2: direct current

    Remarks: set the light source power frequency

*   ## Toupcam_put_Mode, Toupcam_get_Mode

    Return Value: HRESULT type means success/failure

    Parameters:

*   HToupCam h: camera instance handle
*   BOOL bSkip: Bin mode or Skip mode.

> Remarks: set Bin mode or Skip mode. Cameras with higher resolution can support two sampling modes, one is Bin mode (Neighborhood averaging), the other is Skip (sampling extraction). In comparison, the former is with better image effect but decreasing frame rate while the latter is just the reverse.

*   ## Toupcam_put_TempTint, Toupcam_get_TempTint

    Return Value: HRESULT type means success/failure

    Parameters:

*   HToupCam h: camera instance handle
*   int nTemp, int nTint: color temperature and Tint

> Remarks: set/obtain the color temperature and Tint parameters of white balance.
> 
> Toupcam_TempTint2RGB(...) and Toupcam_RGB2TempTint(...) can be used to convert RGB Gain from / to Temp / Tint. This is to say:
> 
> RGB adjustment is equal to TEMP/TINT adjustment. If you want to use the RGB adjustment, you can use the following helper functions.
> 
> <table width="100%" border="0" bgcolor="#B0D0B0">
> 
> <tbody>
> 
> <tr>
> 
> <td>void Toupcam_TempTint2RGB(int nTemp, int nTint, int nRGB[3]);  
> void Toupcam_RGB2TempTint(const int nRGB[3], int* nTemp, int* nTint);</td>
> 
> </tr>
> 
> </tbody>
> 
> </table>
> 
> When setting RGB, please call Toupcam_RGB2TempTint first and translate RGB values to the Temp and Tint value. Then call Toupcam_put_TempTint to set.
> 
> When getting RGB, please call Toupcam_get_TempTint first and get the Temp and Tint value. Then call Toupcam_TempTint2RGB to translate the Temp and Tint to RGB.

*   ## Toupcam_AwbOnePush

    Return Value: HRESULT type means success/failure

    Parameters:

    *   HToupCam h: camera instance handle
    *   PITOUPCAM_TEMPTINT_CALLBACK fnTTProc, void* pTTCtx: callback function and callback context when the automatic white balance completes.

    Remarks: For AWB function, basically there are two methods available in the field. One is continuous AWB mode and the other is one push AWB mode. Continuous AWB mode will do the AWB function all the time and one push AWB mode will do the AWB function once triggered. And toupcam cameras use one push AWB mode because this mode is preferred for microscope industry and more accurate. Continuous AWB mode will introduce some errors in some conditions. Call this function to perform one "auto white balance". When the "auto white balance" completes, TOUPCAM_EVENT_TEMPTINT event notify the application (In Pull Mode) and callback happens. In pull mode, this callback is useless, set it to NULL.

*   ## Toupcam_put_AWBAuxRect, Toupcam_get_AWBAuxRect, Toupcam_put_AEAuxRect, Toupcam_get_AEAuxRect

    Return Value: HRESULT type means success/failure

    Parameters: HToupCam h: camera instance handle

    Remarks: set/obtain the ROI (Rectangle of Interest) of automatic white balance and auto-exposure. The default ROI is in the center of the image, its width is 20% image with, its height is 20% image height.

*   ## Toupcam_get_MonoMode

    Return Value: HRESULT type means success/failure

    Parameters: HToupCam h: camera instance handle

    Remarks: gray camera or not, find the flag in ToupCamModel: TOUPCAM_FLAG_MONO

*   ## Toupcam_get_StillResolutionNumber, Toupcam_get_StillResolution

    Return Value: HRESULT type means success/failure

    Parameters:

    *   HToupCam h: camera instance handle
    *   ULONG nIndex: resolution index
    *   LONG* pWidth, LONG* pHeight: width/height

    Remarks: Toupcam_get_StillResolutionNumber means the number of supported still resolution. Take UCMOS03100KPA as an example, if we call the function Toupcam_get_StillResolutionNumber and get "3", which means it can support three kinds of resolution. If it doesn't support "still snap", then we get "0". Toupcam_get_Resolution obtains the width/height of each kind of resolution.

*   ## Toupcam_get_SerialNumber, Toupcam_get_FwVersion, Toupcam_get_HwVersion

    Return Value: HRESULT type means success/failure

    Parameters:

*   HToupCam h: camera instance handle
*   char sn[32]: buffer to the serial number, such as: TP110826145730ABCD1234FEDC56787
*   char fwver[16]: buffer to the firmware version, such as: 3.2.1.20140922
*   char hwver[16]: buffer to the hardware version, such as: 3.2.1.20140922

> Remarks: each camera has a unique serial number with 31 letters, eg,"TP110826145730ABCD1234FEDC56787"

*   ## Toupcam_put_LEDState

    Return Value: HRESULT type means success/failure

    Parameters:

*   HToupCam h: camera instance handle
*   unsigned short iLed: the index of LED light
*   unsigned short iState: LED status, 1 -> Ever bright; 2 -> Flashing; other -> Off
*   unsigned short iPeriod: Flashing Period (>= 500ms)

> Remarks: One or more LED lights installed on some camera. This function controls the status of these lights.

*   ## Toupcam_read_EEPROM, Toupcam_write_EEPROM

    Return Value: HRESULT type means failure or byte(s) transferred

    Parameters:

*   HToupCam h: camera instance handle
*   unsigned addr: EEPROM address
*   const unsigned char* pData: data to be written
*   unsigned char* pBuffer: read EEPROM to buffer
*   unsigned nDataLen: data length to be written
*   unsigned nBufferLen: buffer length to read

*   ## Toupcam_put_ExpoCallback

    Return Value: HRESULT type means success/failure

    Parameters:

*   HToupCam h: camera instance handle
*   PITOUPCAM_EXPOSURE_CALLBACK fnExpoProc, void* pExpoCtx: exposure callback function and callback context. If we set fnExpoProc as NULL, then it means stop calling back.

> Remarks: Once we set non-NULL callback function, then callback happens whenever the exposure time changes.

*   ## Toupcam_put_ChromeCallback

    Return Value: HRESULT type means success/failure

    Parameters:

*   HToupCam h: camera instance handle
*   PITOUPCAM_CHROME_CALLBACK fnChromeProc, void* pChromeCtx: color/gray switches callback function and callback context. If we set fnChromeProc as NULL, then it means stop calling back.

> Remarks: once we set non-NULL callback function, then callback happens whenever the color/gray switches, eg, call Toupcam_put_Chrome

*   ## Toupcam_LevelRangeAuto

    Return Value: HRESULT type means success/failure

    Parameters: HToupCam h: camera instance handle

    Remarks: auto Level Range.

*   ## Toupcam_put_LevelRange, Toupcam_get_LevelRange

    Return Value: HRESULT type means success/failure

    Parameters:

    *   HToupCam h: camera instance handle
    *   USHORT aLow[4], USHORT aHigh[4]: Level Range of R, G, B, and Gray. RGB is only available for color image, and gray is only available for gray image.

    Remarks: level range related.

*   ## Toupcam_GetHistogram

    Return Value: HRESULT type means success/failure

    Parameters:

*   HToupCam h: camera instance handle
*   PITOUPCAM_HISTOGRAM_CALLBACK fnHistogramProc, void* pHistogramCtx: callback function and callback context of histogram data.

> Remarks: obtain histogram data.

* * *

# <font color="#0000FF">5\. .NET and C# and VB.NET</font>

* * *

Toupcam does support .NET development environment (C# and VB.NET).

toupcam.cs in the 'inc' directory use P/Invoke call into toupcam.dll. Copy toupcam.cs to your C# project, please reference toupcamdemowinformcs in the samples directory.

The C# class ToupTek.ToupCam is a thin wrapper class of the native C/C++ API of toupcam.dll, it's properties and methods P/Invoke into the corresponding Toupcam_xxxx functions of toupcam.dll. So, the descriptions of the Toupcam_xxxx function are also applicable for the corresponding C# properties or methods. For example, the C# Snap method call the function Toupcam_Snap, the descriptions of the Toupcam_Snap function is applicable for C# Snap method:

<table width="100%" border="0" bgcolor="#B0D0B0">

<tbody>

<tr>

<td>[DllImport("toupcam.dll", ExactSpelling = true, CallingConvention = CallingConvention.StdCall)]  
private static extern int Toupcam_Snap(SafeHToupCamHandle h, uint nResolutionIndex);  

public bool Snap(uint nResolutionIndex)  
{  
  if (_handle == null || _handle.IsInvalid || _handle.IsClosed)  
    return false;  
  return (Toupcam_Snap(_handle, nResolutionIndex) >= 0);  
}</td>

</tr>

</tbody>

</table>

VB.NET is similar with C#, not otherwise specified.

* * *

# <font color="#0000FF">6\. Others</font>

* * *

*   Ranges and default value of some parameters

<div align="center">

<table width="50%" border="1" cellpadding="0" cellspacing="0" bgcolor="#B0D0B0">

<tbody>

<tr>

<td width="30%" valign="top">Parameters</td>

<td width="26%" valign="top">Range</td>

<td width="44%" valign="top">Default value</td>

</tr>

<tr>

<td width="30%" valign="top">AutoExpoTarget</td>

<td width="26%" valign="top">10~230</td>

<td width="44%" valign="top">120</td>

</tr>

<tr>

<td width="30%" valign="top">Temp</td>

<td width="26%" valign="top">2000~15000</td>

<td width="44%" valign="top">6503</td>

</tr>

<tr>

<td width="30%" valign="top">Tint</td>

<td width="26%" valign="top">200~2500</td>

<td width="44%" valign="top">1000</td>

</tr>

<tr>

<td width="30%" valign="top">LevelRange</td>

<td width="26%" valign="top">0~255</td>

<td width="44%" valign="top">Low = 0, High = 255</td>

</tr>

<tr>

<td width="30%" valign="top">Contrast</td>

<td width="26%" valign="top">-100~100</td>

<td width="44%" valign="top">0</td>

</tr>

<tr>

<td width="30%" valign="top">Hue</td>

<td width="26%" valign="top">-180~180</td>

<td width="44%" valign="top">0</td>

</tr>

<tr>

<td width="30%" valign="top">Saturation</td>

<td width="26%" valign="top">0~255</td>

<td width="44%" valign="top">128</td>

</tr>

<tr>

<td width="30%" valign="top">Brightness</td>

<td width="26%" valign="top">-64~64</td>

<td width="44%" valign="top">0</td>

</tr>

<tr>

<td width="30%" valign="top">Gamma</td>

<td width="26%" valign="top">20~180</td>

<td width="44%" valign="top">100</td>

</tr>

</tbody>

</table>

</div>

*   Platform
    *   Windows: x86/x64; XP SP3 or above; SSE2 instruction set or above
    *   OSX: x64; 10.7 or above
    *   Linux: SSE3 instruction set or above; kernel 2.6.27 (Released in October 2008) or above
        *   x86: GLIBC 2.9 (Released in November 2008) or above
        *   x64: GLIBC 2.14 (Released in June 2011) or above

* * *

# <font color="#0000FF">7\. Changelog</font>

* * *

v1.1: support RAW format; support Linux and osx

v1.0: initial release

* * *

# <font color="#0000FF">8\. Contact Information</font>

* * *

If you have any problems in using this SDK, please use the following information to contact us.  
www: [www.touptek.com](http://www.touptek.com)  
email: support@touptek.com