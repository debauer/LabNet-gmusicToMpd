# LabNet-gmusicToMpd
======================

Just a litte script to simplify the gmusicproxy url requests.

Requiremtents
----------------------

  * google music unlimited account
  * gmusicproxy -> http://gmusicproxy.net/


Routes
----------------------

### /play/album/<string:artist>/<string:album>

#### [GET]
return the extm3u and play it via MPD on the LabNet-Server

##### Response Codes
| Status | Code                         | Description                                     |
|--------|------------------------------|-------------------------------------------------|
| 201    | OK                           |                                                 |
| 400    |                              |                                                 |
| 409    |                              |                                                 |
| 500    |                              |                                                 |

### /add/album/<string:artist>/<string:album>

#### [GET]
return the extm3u and append it to the MPD Playlist on the LabNet-Server

##### Response Codes
| Status | Code                         | Description                                     |
|--------|------------------------------|-------------------------------------------------|
| 201    | OK                           |                                                 |
| 400    |                              |                                                 |
| 409    |                              |                                                 |
| 500    |                              |                                                 |

### /play/radio/<string:artist>

#### [GET]
return the extm3u and play it via MPD on the LabNet-Server

##### Response Codes
| Status | Code                         | Description                                     |
|--------|------------------------------|-------------------------------------------------|
| 201    | OK                           |                                                 |
| 400    |                              |                                                 |
| 409    |                              |                                                 |
| 500    |                              |                                                 |

### /add/radio/<string:artist>

#### [GET]
return the extm3u and append it to the MPD Playlist on the LabNet-Server

##### Response Codes
| Status | Code                         | Description                                     |
|--------|------------------------------|-------------------------------------------------|
| 201    | OK                           |                                                 |
| 400    |                              |                                                 |
| 409    |                              |                                                 |
| 500    |                              |                                                 |