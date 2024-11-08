[ElevenLabs home page![light logo](https://mintlify.s3-us-west-1.amazonaws.com/elevenlabs-docs/logo/favicon.png)![dark logo](https://mintlify.s3-us-west-1.amazonaws.com/elevenlabs-docs/logo/favicon.png)](/docs)

Search or ask...

Ctrl K

  * [Sign Up](https://elevenlabs.io/sign-up)
  * [Text to Speech](https://elevenlabs.io/text-to-speech)
  * [Help Center](https://help.elevenlabs.io/)
  * [Sign Up](https://elevenlabs.io/sign-up)



Search...

Navigation

VOICES

Default Voices

* [Documentation](/docs/introduction)
* [API Reference](/docs/api-reference/getting-started)
* [Conversational AI SDKs](/docs/conversational-ai-sdks/conversational-ai-guide)
* [Python Library](https://github.com/elevenlabs/elevenlabs-python)
* [JavaScript Library](https://github.com/elevenlabs/elevenlabs-js)
* [Community](https://discord.gg/elevenlabs)
* [Guides](/docs/guides/getting-started)
* [Release Notes](/docs/release-notes/product-updates)

GETTING STARTED

  * [Introduction](/docs/introduction)



CREATE

  * Text to Speech (Speech Synthesis)

  * Speech to Speech (Voice Changer)

  * Sound Effects




VOICES

  * [Overview](/docs/voices/overview)
  * [Default Voices](/docs/voices/default-voices)
  * [Voice Design](/docs/voices/voice-lab/voice-design)
  * Voice Cloning

  * Voice Library




WORKFLOWS

  * Projects

  * Dubbing Studio

  * Voiceover Studio

  * Conversational AI

  * Audio Native




WORKSPACE

  * [Overview](/docs/workspace/overview)
  * [SSO Setup](/docs/workspace/sso_setup)



TROUBLESHOOTING

  * [Overview](/docs/troubleshooting/overview)



VOICES

Default Voices

A curated set of voices for our core use cases.

Default voices are a curated set of voices optimized for our core use cases and made available to all ElevenLabs users by default. They come with a few core guarantees:

  * **Long-term availability** : we make our default voices via multi-year partnerships with voice actors
  * **Consistent quality** : our team carefully crafts and QCs our default voices to ensure they perform well across a range of use cases
  * **Priority model support** : our default voices are the first to receive fine tunings for new models as they are released



**Note:** Default voices were previously referred to as “premade” voices. The latter term is still used when accessing default voices via the API, e.g. when filtering by `category == "premade"`. Please see the [voices API documentation](https://elevenlabs.io/docs/api-reference/get-voices) for more details.

[​](#using-default-voices)

Using Default Voices

Unlike voices you add from the Voice Library or new [Instant Voice Clones (IVCs)](/docs/voices/voice-lab/instant-voice-cloning) or [Professional Voice Clones (PVCs)](/docs/voices/voice-lab/professional-voice-cloning) you create, default voices are not accessed via your [My Voices](/docs/voices/voice-lab/overview).

There are several ways you can find and use default voices:

Instead, there are 2 ways to find and use default voices:

  * **My Voices** : Default voices can be found in My Voices, under either the “All” or the “Default” tabs. Default voices do not take up any of your custom voice slots, and cannot be removed from My Voices. You can use Default voices directly from My Voices by clicking “Use”. This will open Speech Synthesis with the voice already selected.

  * **API** : Calls to the /voices endpoint will fetch all default voices in addition to voices added to My Voices. See the [ voices API documentation ](https://elevenlabs.io/docs/api-reference/get-voices) for more details. 

  * **Voice dropdown menu** : Default voices can be selected from the voice dropdown menu. In Speech Synthesis, this can be accessed by clicking the voice name in the bottom left-hand corner of the text-to-speech or voice changer screen:

![](https://mintlify.s3-us-west-1.amazonaws.com/elevenlabs-docs/voices/images/voice-select.png)

You’ll find our default voices under the “Default” heading, or alternatively, you can search for the name of the voice you want to use. To hear a sample of the voice, click the circular icon next to the voice name.

![](https://mintlify.s3-us-west-1.amazonaws.com/elevenlabs-docs/voices/images/default-voices.png)



[​](#current-default-voices)

Current Default Voices

Below is a list of our current default voices, including metadata and sample audio. Please note that all of our current default voices have fine tunings for our **Turbo v2, Turbo v2.5, and Multilingual v2 models** , which means they are optimized for use with these models.

name| voice_id| gender| age| accent| description| use_case| preview_url  
---|---|---|---|---|---|---|---  
Alice| Xb7hH8MSUJpSbSDYk0k2| female| middle-aged| British| confident| news| [Sample](https://storage.googleapis.com/eleven-public-prod/premade/voices/Xb7hH8MSUJpSbSDYk0k2/d10f7534-11f6-41fe-a012-2de1e482d336.mp3)  
Aria| 9BWtsMINqrJLrRacOk9x| female| middle-aged| American| expressive| social media| [Sample](https://storage.googleapis.com/eleven-public-prod/premade/voices/9BWtsMINqrJLrRacOk9x/405766b8-1f4e-4d3c-aba1-6f25333823ec.mp3)  
Bill| pqHfZKP75CvOlQylNhV4| male| old| American| trustworthy| narration| [Sample](https://storage.googleapis.com/eleven-public-prod/premade/voices/pqHfZKP75CvOlQylNhV4/d782b3ff-84ba-4029-848c-acf01285524d.mp3)  
Brian| nPczCjzI2devNBz1zQrb| male| middle-aged| American| deep| narration| [Sample](https://storage.googleapis.com/eleven-public-prod/premade/voices/nPczCjzI2devNBz1zQrb/2dd3e72c-4fd3-42f1-93ea-abc5d4e5aa1d.mp3)  
Callum| N2lVS1w4EtoT3dr4eOWO| male| middle-aged| Transatlantic| intense| characters| [Sample](https://storage.googleapis.com/eleven-public-prod/premade/voices/N2lVS1w4EtoT3dr4eOWO/ac833bd8-ffda-4938-9ebc-b0f99ca25481.mp3)  
Charlie| IKne3meq5aSn9XLyUdCD| male| middle aged| Australian| natural| conversational| [Sample](https://storage.googleapis.com/eleven-public-prod/premade/voices/IKne3meq5aSn9XLyUdCD/102de6f2-22ed-43e0-a1f1-111fa75c5481.mp3)  
Charlotte| XB0fDUnXU5powFXDhCwa| female| young| Swedish| seductive| characters| [Sample](https://storage.googleapis.com/eleven-public-prod/premade/voices/XB0fDUnXU5powFXDhCwa/942356dc-f10d-4d89-bda5-4f8505ee038b.mp3)  
Chris| iP95p4xoKVk53GoZ742B| male| middle-aged| American| casual| conversational| [Sample](https://storage.googleapis.com/eleven-public-prod/premade/voices/iP95p4xoKVk53GoZ742B/3f4bde72-cc48-40dd-829f-57fbf906f4d7.mp3)  
Daniel| onwK4e9ZLuTAKqWW03F9| male| middle-aged| British| authoritative| news| [Sample](https://storage.googleapis.com/eleven-public-prod/premade/voices/onwK4e9ZLuTAKqWW03F9/7eee0236-1a72-4b86-b303-5dcadc007ba9.mp3)  
Eric| cjVigY5qzO86Huf0OWal| male| middle-aged| American| friendly| conversational| [Sample](https://storage.googleapis.com/eleven-public-prod/premade/voices/cjVigY5qzO86Huf0OWal/d098fda0-6456-4030-b3d8-63aa048c9070.mp3)  
George| JBFqnCBsd6RMkjVDRZzb| male| middle aged| British| warm| narration| [Sample](https://storage.googleapis.com/eleven-public-prod/premade/voices/JBFqnCBsd6RMkjVDRZzb/e6206d1a-0721-4787-aafb-06a6e705cac5.mp3)  
Jessica| cgSgspJ2msm6clMCkdW9| female| young| American| expressive| conversational| [Sample](https://storage.googleapis.com/eleven-public-prod/premade/voices/cgSgspJ2msm6clMCkdW9/56a97bf8-b69b-448f-846c-c3a11683d45a.mp3)  
Laura| FGY2WhTYpPnrIDTdsKH5| female| young| American| upbeat| social media| [Sample](https://storage.googleapis.com/eleven-public-prod/premade/voices/FGY2WhTYpPnrIDTdsKH5/67341759-ad08-41a5-be6e-de12fe448618.mp3)  
Liam| TX3LPaxmHKxFdv7VOQHJ| male| young| American| articulate| narration| [Sample](https://storage.googleapis.com/eleven-public-prod/premade/voices/TX3LPaxmHKxFdv7VOQHJ/63148076-6363-42db-aea8-31424308b92c.mp3)  
Lily| pFZP5JQG7iQjIQuC4Bku| female| middle-aged| British| warm| narration| [Sample](https://storage.googleapis.com/eleven-public-prod/premade/voices/pFZP5JQG7iQjIQuC4Bku/89b68b35-b3dd-4348-a84a-a3c13a3c2b30.mp3)  
Matilda| XrExE9yKIg1WjnnlVkGX| female| middle-aged| American| friendly| narration| [Sample](https://storage.googleapis.com/eleven-public-prod/premade/voices/XrExE9yKIg1WjnnlVkGX/b930e18d-6b4d-466e-bab2-0ae97c6d8535.mp3)  
River| SAz9YHcvj6GT2YYXdXww| non-binary| middle-aged| American| confident| social media| [Sample](https://storage.googleapis.com/eleven-public-prod/premade/voices/SAz9YHcvj6GT2YYXdXww/e6c95f0b-2227-491a-b3d7-2249240decb7.mp3)  
Roger| CwhRBWXzGAHq8TQ4Fs17| male| middle-aged| American| confident| social media| [Sample](https://storage.googleapis.com/eleven-public-prod/premade/voices/CwhRBWXzGAHq8TQ4Fs17/58ee3ff5-f6f2-4628-93b8-e38eb31806b0.mp3)  
Sarah| EXAVITQu4vr4xnSDxMaL| female| young| American| soft| news| [Sample](https://storage.googleapis.com/eleven-public-prod/premade/voices/EXAVITQu4vr4xnSDxMaL/01a3e33c-6e99-4ee7-8543-ff2216a32186.mp3)  
Will| bIHbv24MWmeRgasZH58o| male| young| American| friendly| social media| [Sample](https://storage.googleapis.com/eleven-public-prod/premade/voices/bIHbv24MWmeRgasZH58o/8caf8f3d-ad29-4980-af41-53f20c72d7a4.mp3)  
  
[​](#how-do-default-voices-sound-in-my-language)

How do Default Voices sound in my language?

  * Our default voices can be used to generate audio in any of the [32 languages we support](https://elevenlabs.io/docs/api-reference/text-to-speech#supported-languages) by using them with one of our multilingual models (e.g. Multilingual v2 or Turbo v2.5).
  * Some default voices may have unpredicable accents in other languages.
  * We are working to provide a granular overview of how each default voice sounds in each of the languages we support and will update this page when this is ready.



[​](#legacy-voices)

Legacy Voices

Below is a list of our legacy voices, which can be accesssed in 2 ways:

  * **UI** : Search for the name of the legacy voice you’re looking for in any voice dropdown, or go to My Voices -> Default, and look for voices with “Legacy” in the name.
  * **API** : To see legacy voices when calling the /voices endpoint, you need to set the `show_legacy` query parameter to `True`. Please see the [voices API documentation](https://elevenlabs.io/docs/api-reference/get-voices) for more details.



**Note:** Legacy voices will remain available for the foreseeable future, but they are less consistent than default voices and will not receive priority support for future model releases. For more information on Legacy voices, please see [What are Legacy voices?](https://help.elevenlabs.io/hc/en-us/articles/26928417254801-What-are-Legacy-voices)

name| voice_id| gender| age| accent| description| use_case| preview_url  
---|---|---|---|---|---|---|---  
Adam| pNInz6obpgDQGcFmaJgB| male| middle aged| american| deep| narration| [Sample](https://storage.googleapis.com/eleven-public-prod/premade/voices/pNInz6obpgDQGcFmaJgB/d6905d7a-dd26-4187-bfff-1bd3a5ea7cac.mp3)  
Antoni| ErXwobaYiN019PkySvjV| male| young| american| well-rounded| narration| [Sample](https://storage.googleapis.com/eleven-public-prod/premade/voices/ErXwobaYiN019PkySvjV/2d5ab2a3-4578-470f-b797-6331e46a7d55.mp3)  
Arnold| VR6AewLTigWG4xSOukaG| male| middle aged| american| crisp| narration| [Sample](https://storage.googleapis.com/eleven-public-prod/premade/voices/VR6AewLTigWG4xSOukaG/49a22885-80d5-48e8-87a3-076fc9193d9a.mp3)  
Clyde| 2EiwWnXFnvU5JabPnv8n| male| middle-aged| American| war veteran| characters| [Sample](https://storage.googleapis.com/eleven-public-prod/premade/voices/2EiwWnXFnvU5JabPnv8n/65d80f52-703f-4cae-a91d-75d4e200ed02.mp3)  
Dave| CYw3kZ02Hs0563khs1Fj| male| young| British| conversational| characters| [Sample](https://storage.googleapis.com/eleven-public-prod/premade/voices/CYw3kZ02Hs0563khs1Fj/872cb056-45d3-419e-b5c6-de2b387a93a0.mp3)  
Dorothy| ThT5KcBeYPX3keUQqHPh| female| young| British| pleasant| narration| [Sample](https://storage.googleapis.com/eleven-public-prod/premade/voices/ThT5KcBeYPX3keUQqHPh/981f0855-6598-48d2-9f8f-b6d92fbbe3fc.mp3)  
Drew| 29vD33N1CtxCmqQRPOHJ| male| middle-aged| American| well-rounded| news| [Sample](https://storage.googleapis.com/eleven-public-prod/premade/voices/29vD33N1CtxCmqQRPOHJ/b99fc51d-12d3-4312-b480-a8a45a7d51ef.mp3)  
Emily| LcfcDJNUP1GQjkzn1xUU| female| young| American| calm| meditation| [Sample](https://storage.googleapis.com/eleven-public-prod/premade/voices/LcfcDJNUP1GQjkzn1xUU/e4b994b7-9713-4238-84f3-add8fccaaccd.mp3)  
Ethan| g5CIjZEefAph4nQFvHAz| male| young| American| soft| ASMR| [Sample](https://storage.googleapis.com/eleven-public-prod/premade/voices/g5CIjZEefAph4nQFvHAz/26acfa99-fdec-43b8-b2ee-e49e75a3ac16.mp3)  
Fin| D38z5RcWu1voky8WS1ja| male| old| Irish| sailor| characters| [Sample](https://storage.googleapis.com/eleven-public-prod/premade/voices/D38z5RcWu1voky8WS1ja/a470ba64-1e72-46d9-ba9d-030c4155e2d2.mp3)  
Freya| jsCqWAovK2LkecY7zXl4| female| young| American| expressive| characters| [Sample](https://storage.googleapis.com/eleven-public-prod/premade/voices/jsCqWAovK2LkecY7zXl4/8e1f5240-556e-4fd5-892c-25df9ea3b593.mp3)  
George| Yko7PKHZNXotIFUBG7I9| male| middle aged| british| audiobook| [Sample](https://storage.googleapis.com/eleven-public-prod/premade/voices/Yko7PKHZNXotIFUBG7I9/02c66c93-a237-436f-8a7d-43e8c49bc6a3.mp3)  
Gigi| jBpfuIE2acCO8z3wKNLl| female| young| American| childlish| animation| [Sample](https://storage.googleapis.com/eleven-public-prod/premade/voices/jBpfuIE2acCO8z3wKNLl/3a7e4339-78fa-404e-8d10-c3ef5587935b.mp3)  
Giovanni| zcAOhNBS3c14rBihAFp1| male| young| Italian| foreigner| narration| [Sample](https://storage.googleapis.com/eleven-public-prod/premade/voices/zcAOhNBS3c14rBihAFp1/e7410f8f-4913-4cb8-8907-784abee5aff8.mp3)  
Glinda| z9fAnlkpzviPz146aGWa| female| middle-aged| American| witch| characters| [Sample](https://storage.googleapis.com/eleven-public-prod/premade/voices/z9fAnlkpzviPz146aGWa/cbc60443-7b61-4ebb-b8e1-5c03237ea01d.mp3)  
Grace| oWAxZDx7w5VEj9dCyTzz| female| young| American (South)| pleasant| narration| [Sample](https://storage.googleapis.com/eleven-public-prod/premade/voices/oWAxZDx7w5VEj9dCyTzz/84a36d1c-e182-41a8-8c55-dbdd15cd6e72.mp3)  
Harry| SOYHLrjzK2X1ezoPC6cr| male| young| American| anxious| characters| [Sample](https://storage.googleapis.com/eleven-public-prod/premade/voices/SOYHLrjzK2X1ezoPC6cr/86d178f6-f4b6-4e0e-85be-3de19f490794.mp3)  
James| ZQe5CZNOzWyzPSCn5a3c| male| old| Australian| calm| news| [Sample](https://storage.googleapis.com/eleven-public-prod/premade/voices/ZQe5CZNOzWyzPSCn5a3c/35734112-7b72-48df-bc2f-64d5ab2f791b.mp3)  
Jeremy| bVMeCyTHy58xNoL34h3p| male| young| Irish| excited| narration| [Sample](https://storage.googleapis.com/eleven-public-prod/premade/voices/bVMeCyTHy58xNoL34h3p/66c47d58-26fd-4b30-8a06-07952116a72c.mp3)  
Jessie| t0jbNlBVZ17f02VDIeMI| male| old| American| raspy| characters| [Sample](https://storage.googleapis.com/eleven-public-prod/premade/voices/t0jbNlBVZ17f02VDIeMI/e26939e3-61a4-4872-a41d-33922cfbdcdc.mp3)  
Joseph| Zlb1dXrM653N07WRdFW3| male| middle-aged| British| articulate| news| [Sample](https://storage.googleapis.com/eleven-public-prod/premade/voices/Zlb1dXrM653N07WRdFW3/daa22039-8b09-4c65-b59f-c79c48646a72.mp3)  
Josh| TxGEqnHWrfWFTfGW9XjX| male| young| american| deep| narration| [Sample](https://storage.googleapis.com/eleven-public-prod/premade/voices/TxGEqnHWrfWFTfGW9XjX/47de9a7e-773a-42a8-b410-4aa90c581216.mp3)  
Michael| flq6f7yk4E4fJM5XTYuZ| male| old| American| calm| narration| [Sample](https://storage.googleapis.com/eleven-public-prod/premade/voices/flq6f7yk4E4fJM5XTYuZ/c6431a82-f7d2-4905-b8a4-a631960633d6.mp3)  
Mimi| zrHiDhphv9ZnVXBqCLjz| female| young| Swedish| childish| animation| [Sample](https://storage.googleapis.com/eleven-public-prod/premade/voices/zrHiDhphv9ZnVXBqCLjz/decbf20b-0f57-4fac-985b-a4f0290ebfc4.mp3)  
Nicole| piTKgcLEGmPE4e6mEKli| female| young| American| soft| ASMR| [Sample](https://storage.googleapis.com/eleven-public-prod/premade/voices/piTKgcLEGmPE4e6mEKli/c269a54a-e2bc-44d0-bb46-4ed2666d6340.mp3)  
Patrick| ODq5zmih8GrVes37Dizd| male| middle-aged| American| shouty| characters| [Sample](https://storage.googleapis.com/eleven-public-prod/premade/voices/ODq5zmih8GrVes37Dizd/0ebec87a-2569-4976-9ea5-0170854411a9.mp3)  
Paul| 5Q0t7uMcjvnagumLfvZi| male| middle-aged| American| authoritative| news| [Sample](https://storage.googleapis.com/eleven-public-prod/premade/voices/5Q0t7uMcjvnagumLfvZi/a4aaa30e-54c4-44a4-8e46-b9b00505d963.mp3)  
Rachel| 21m00Tcm4TlvDq8ikWAM| female| young| american| calm| narration| [Sample](https://storage.googleapis.com/eleven-public-prod/premade/voices/21m00Tcm4TlvDq8ikWAM/b4928a68-c03b-411f-8533-3d5c299fd451.mp3)  
Sam| yoZ06aMxZJJ28mfd3POQ| male| young| american| raspy| narration| [Sample](https://storage.googleapis.com/eleven-public-prod/premade/voices/yoZ06aMxZJJ28mfd3POQ/b017ad02-8d18-4456-ad92-55c85ecf6363.mp3)  
Serena| pMsXgVXv3BLzUgSXRplE| female| middle-aged| American| pleasant| narration| [Sample](https://storage.googleapis.com/eleven-public-prod/premade/voices/pMsXgVXv3BLzUgSXRplE/d61f18ed-e5b0-4d0b-a33c-5c6e7e33b053.mp3)  
Thomas| GBv7mTt0atIp3Br8iCZE| male| young| American| calm| meditation| [Sample](https://storage.googleapis.com/eleven-public-prod/premade/voices/GBv7mTt0atIp3Br8iCZE/98542988-5267-4148-9a9e-baa8c4f14644.mp3)  
  
[Suggest edits](https://github.com/elevenlabs/elevenlabs-docs/edit/main/voices/default-voices.mdx)[Raise issue](https://github.com/elevenlabs/elevenlabs-docs/issues/new?title=Issue on docs&body=Path: /voices/default-voices)

[Overview](/docs/voices/overview)[Voice Design](/docs/voices/voice-lab/voice-design)

[linkedin](https://www.linkedin.com/company/elevenlabsio)[twitter](https://twitter.com/elevenlabsio)[discord](https://discord.gg/ZcPfAy3xSE)[youtube](https://www.youtube.com/channel/UC-ew9TfeD887qUSiWWAAj1w)[github](https://github.com/elevenlabs)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=docs&utm_source=elevenlabs-docs)

On this page

  * [Using Default Voices](#using-default-voices)
  * [Current Default Voices](#current-default-voices)
  * [How do Default Voices sound in my language?](#how-do-default-voices-sound-in-my-language)
  * [Legacy Voices](#legacy-voices)



Terms and conditions

By clicking "Continue," I agree to the Terms of Service, acknowledge ElevenLabs' Privacy Policy. 

I consent to the recording, collection and use of my voice and data derived from my voice to interpret my speech and provide customer support services. 

I consent to sharing my voice and data derived from my voice with third-party service providers to train and improve our customer support models. 

I understand that if I do not consent to the collection as described above, ElevenLabs services cannot be provided to me. 

![](https://mintlify.s3-us-west-1.amazonaws.com/elevenlabs-docs/voices/images/voice-select.png)