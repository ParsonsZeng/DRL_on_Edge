BOTTOM = 0
def ID():
    global BOTTOM
    BOTTOM+=1
    return BOTTOM

TYPE_COM_IOT2SERVER_MEDIAS              = ID()
TYPE_COM_IOT2SERVER_MODEL_PARAMETER     = ID()
TYPE_COM_IOT2SERVER_MODEL_GRADIENTS     = ID()
TYPE_COM_IOT2SERVER_REWARDS             = ID()
TYPE_COM_SERVER2IOT_MODEL_PARAMETERS    = ID()
TYPE_COM_SERVER2IOT_ACTIONS             = ID()
TYPE_COM_SERVER2IOT_MODEL_GRADIENTS     = ID()
TYPE_COM_SERVER2SERVER_MODEL_PARAMETER  = ID()
TYPE_COM_SERVER2SERVER_MODEL_GRADIENTS  = ID()

TYPE_JOB_SERVER_INFERENCE               = ID()
TYPE_JOB_SERVER_BACKWARD                = ID()
TYPE_JOB_IOT_INFERENCE                  = ID()
TYPE_JOB_IOT_BACKWARD                   = ID()
TYPE_JOB_IOT_ACT                        = ID()
TYPE_JOB_SERVER_INFERENCE               = ID()
TYPE_JOB_SERVER_BACKWARD                = ID()
TYPE_JOB_SERVER_SYNC_GRADIENTS          = ID()

