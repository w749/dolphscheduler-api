from attr import attrs, attrib


@attrs
class Inner(object):
    pass


@attrs
class GetSessionIdInner(Inner):
    securityConfigType = attrib(type=str, default="")
    sessionId = attrib(type=str, default="")


@attrs
class CreateTokenInner(Inner):
    id = attrib(type=int, default=-1)
    userId = attrib(type=int, default=-1)
    token = attrib(type=str, default="")
    expireTime = attrib(type=str, default="")
    createTime = attrib(type=str, default="")
    updateTime = attrib(type=str, default="")
    userName = attrib(type=str, default="")


@attrs
class TenantInner(Inner):
    id = attrib(type=int, default=-1)
    tenantCode = attrib(type=str, default="")
    description = attrib(type=str, default="")
    queueId = attrib(type=int, default=-1)
    queueName = attrib(type=str, default="")
    queue = attrib(type=str, default="")
    createTime = attrib(type=str, default="")
    updateTime = attrib(type=str, default="")


@attrs
class QueueInner(Inner):
    id = attrib(type=int, default=-1)
    queueName = attrib(type=str, default="")
    queue = attrib(type=str, default="")
    createTime = attrib(type=str, default="")
    updateTime = attrib(type=str, default="")


@attrs
class ProjectInner(Inner):
    id = attrib(type=int, default=-1)
    userId = attrib(type=int, default=-1)
    userName = attrib(type=str, default="")
    code = attrib(type=int, default=-1)
    name = attrib(type=str, default="")
    description = attrib(type=str, default="")
    createTime = attrib(type=str, default="")
    updateTime = attrib(type=str, default="")
    perm = attrib(type=int, default=-1)
    defCount = attrib(type=int, default=-1)
    instRunningCount = attrib(type=int, default=-1)


@attrs
class ResourceInner(Inner):
    id = attrib(type=int, default=-1)
    pid = attrib(type=str, default="")
    name = attrib(type=str, default="")
    fullName = attrib(type=str, default="")
    description = attrib(type=str, default="")
    children = attrib(type=list, default=[])
    type = attrib(type=str, default="")
    currentDir = attrib(type=str, default="")
    idValue = attrib(type=str, default="")
    dirctory = attrib(type=bool, default=False)


@attrs
class SchedulerInner(Inner):
    id = attrib(type=int, default=-1)
    processDefinitionCode = attrib(type=int, default=-1)
    processDefinitionName = attrib(type=str, default="")
    projectName = attrib(type=str, default="")
    definitionDescription = attrib(type=str, default="")
    startTime = attrib(type=str, default="")
    endTime = attrib(type=str, default="")
    timezoneId = attrib(type=str, default="")
    crontab = attrib(type=str, default="")
    failureStrategy = attrib(type=str, default="")
    warningType = attrib(type=str, default="")
    createTime = attrib(type=str, default="")
    updateTime = attrib(type=str, default="")
    userId = attrib(type=int, default=-1)
    userName = attrib(type=str, default="")
    releaseState = attrib(type=str, default="")
    warningGroupId = attrib(type=int, default=-1)
    processInstancePriority = attrib(type=str, default="")
    workerGroup = attrib(type=str, default="")
    tenantCode = attrib(type=str, default="")
    environmentCode = attrib(type=int, default=-1)
    environmentName = attrib(type=str, default="")
