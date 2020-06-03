#
# Autogenerated by Thrift Compiler (0.13.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py:slots
#
import sys

from thrift.protocol.TProtocol import TProtocolException
from thrift.Thrift import TApplicationException
from thrift.Thrift import TException
from thrift.Thrift import TFrozenDict
from thrift.Thrift import TMessageType
from thrift.Thrift import TType
from thrift.transport import TTransport
from thrift.TRecursive import fix_spec

all_structs = []


class ErrorCode(object):
    """
    The integer values within this enum correspond to HTTP status codes.

    HTTP layers can easily map errors to an appropriate status code.

    """

    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    PAYMENT_REQUIRED = 402
    FORBIDDEN = 403
    NOT_FOUND = 404
    CONFLICT = 409
    GONE = 410
    PRECONDITION_FAILED = 412
    PAYLOAD_TOO_LARGE = 413
    IM_A_TEAPOT = 418
    MISDIRECTED_REQUEST = 421
    UNPROCESSABLE_ENTITY = 422
    LOCKED = 423
    FAILED_DEPENDENCY = 424
    TOO_EARLY = 425
    PRECONDITION_REQUIRED = 428
    TOO_MANY_REQUESTS = 429
    REQUEST_HEADER_FIELDS_TOO_LARGE = 431
    UNAVAILABLE_FOR_LEGAL_REASONS = 451
    INTERNAL_SERVER_ERROR = 500
    NOT_IMPLEMENTED = 501
    BAD_GATEWAY = 502
    SERVICE_UNAVAILABLE = 503
    TIMEOUT = 504
    INSUFFICIENT_STORAGE = 507
    LOOP_DETECTED = 508
    USER_DEFINED = 1000

    _VALUES_TO_NAMES = {
        400: "BAD_REQUEST",
        401: "UNAUTHORIZED",
        402: "PAYMENT_REQUIRED",
        403: "FORBIDDEN",
        404: "NOT_FOUND",
        409: "CONFLICT",
        410: "GONE",
        412: "PRECONDITION_FAILED",
        413: "PAYLOAD_TOO_LARGE",
        418: "IM_A_TEAPOT",
        421: "MISDIRECTED_REQUEST",
        422: "UNPROCESSABLE_ENTITY",
        423: "LOCKED",
        424: "FAILED_DEPENDENCY",
        425: "TOO_EARLY",
        428: "PRECONDITION_REQUIRED",
        429: "TOO_MANY_REQUESTS",
        431: "REQUEST_HEADER_FIELDS_TOO_LARGE",
        451: "UNAVAILABLE_FOR_LEGAL_REASONS",
        500: "INTERNAL_SERVER_ERROR",
        501: "NOT_IMPLEMENTED",
        502: "BAD_GATEWAY",
        503: "SERVICE_UNAVAILABLE",
        504: "TIMEOUT",
        507: "INSUFFICIENT_STORAGE",
        508: "LOOP_DETECTED",
        1000: "USER_DEFINED",
    }

    _NAMES_TO_VALUES = {
        "BAD_REQUEST": 400,
        "UNAUTHORIZED": 401,
        "PAYMENT_REQUIRED": 402,
        "FORBIDDEN": 403,
        "NOT_FOUND": 404,
        "CONFLICT": 409,
        "GONE": 410,
        "PRECONDITION_FAILED": 412,
        "PAYLOAD_TOO_LARGE": 413,
        "IM_A_TEAPOT": 418,
        "MISDIRECTED_REQUEST": 421,
        "UNPROCESSABLE_ENTITY": 422,
        "LOCKED": 423,
        "FAILED_DEPENDENCY": 424,
        "TOO_EARLY": 425,
        "PRECONDITION_REQUIRED": 428,
        "TOO_MANY_REQUESTS": 429,
        "REQUEST_HEADER_FIELDS_TOO_LARGE": 431,
        "UNAVAILABLE_FOR_LEGAL_REASONS": 451,
        "INTERNAL_SERVER_ERROR": 500,
        "NOT_IMPLEMENTED": 501,
        "BAD_GATEWAY": 502,
        "SERVICE_UNAVAILABLE": 503,
        "TIMEOUT": 504,
        "INSUFFICIENT_STORAGE": 507,
        "LOOP_DETECTED": 508,
        "USER_DEFINED": 1000,
    }


class Loid(object):
    """
    The components of the Reddit LoID cookie that we want to propagate between
    services.

    This model is a component of the "Edge-Request" header.  You should not need to
    interact with this model directly, but rather through the EdgeRequestContext
    interface provided by baseplate.


    Attributes:
     - id: The ID of the LoID cookie.

     - created_ms: The time when the LoID cookie was created in epoch milliseconds.


    """

    __slots__ = ("id", "created_ms")

    def __init__(self, id=None, created_ms=None):
        self.id = id
        self.created_ms = created_ms

    def read(self, iprot):
        if (
            iprot._fast_decode is not None
            and isinstance(iprot.trans, TTransport.CReadableTransport)
            and self.thrift_spec is not None
        ):
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.id = (
                        iprot.readString().decode("utf-8")
                        if sys.version_info[0] == 2
                        else iprot.readString()
                    )
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I64:
                    self.created_ms = iprot.readI64()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin("Loid")
        if self.id is not None:
            oprot.writeFieldBegin("id", TType.STRING, 1)
            oprot.writeString(self.id.encode("utf-8") if sys.version_info[0] == 2 else self.id)
            oprot.writeFieldEnd()
        if self.created_ms is not None:
            oprot.writeFieldBegin("created_ms", TType.I64, 2)
            oprot.writeI64(self.created_ms)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ["%s=%r" % (key, getattr(self, key)) for key in self.__slots__]
        return "%s(%s)" % (self.__class__.__name__, ", ".join(L))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        for attr in self.__slots__:
            my_val = getattr(self, attr)
            other_val = getattr(other, attr)
            if my_val != other_val:
                return False
        return True

    def __ne__(self, other):
        return not (self == other)


class Session(object):
    """
    The components of the Reddit Session tracker cookie that we want to
    propagate between services.

    This model is a component of the "Edge-Request" header.  You should not need to
    interact with this model directly, but rather through the EdgeRequestContext
    interface provided by baseplate.


    Attributes:
     - id: The ID of the Session tracker cookie.


    """

    __slots__ = ("id",)

    def __init__(self, id=None):
        self.id = id

    def read(self, iprot):
        if (
            iprot._fast_decode is not None
            and isinstance(iprot.trans, TTransport.CReadableTransport)
            and self.thrift_spec is not None
        ):
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.id = (
                        iprot.readString().decode("utf-8")
                        if sys.version_info[0] == 2
                        else iprot.readString()
                    )
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin("Session")
        if self.id is not None:
            oprot.writeFieldBegin("id", TType.STRING, 1)
            oprot.writeString(self.id.encode("utf-8") if sys.version_info[0] == 2 else self.id)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ["%s=%r" % (key, getattr(self, key)) for key in self.__slots__]
        return "%s(%s)" % (self.__class__.__name__, ", ".join(L))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        for attr in self.__slots__:
            my_val = getattr(self, attr)
            other_val = getattr(other, attr)
            if my_val != other_val:
                return False
        return True

    def __ne__(self, other):
        return not (self == other)


class Device(object):
    """
    The components of the device making a request to our services that we want to
    propogate between services.

    This model is a component of the "Edge-Request" header.  You should not need to
    interact with this model directly, but rather through the EdgeRequestContext
    interface provided by baseplate.


    Attributes:
     - id: The ID of the device.


    """

    __slots__ = ("id",)

    def __init__(self, id=None):
        self.id = id

    def read(self, iprot):
        if (
            iprot._fast_decode is not None
            and isinstance(iprot.trans, TTransport.CReadableTransport)
            and self.thrift_spec is not None
        ):
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.id = (
                        iprot.readString().decode("utf-8")
                        if sys.version_info[0] == 2
                        else iprot.readString()
                    )
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin("Device")
        if self.id is not None:
            oprot.writeFieldBegin("id", TType.STRING, 1)
            oprot.writeString(self.id.encode("utf-8") if sys.version_info[0] == 2 else self.id)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ["%s=%r" % (key, getattr(self, key)) for key in self.__slots__]
        return "%s(%s)" % (self.__class__.__name__, ", ".join(L))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        for attr in self.__slots__:
            my_val = getattr(self, attr)
            other_val = getattr(other, attr)
            if my_val != other_val:
                return False
        return True

    def __ne__(self, other):
        return not (self == other)


class OriginService(object):
    """
    Metadata about the origin service for a request.

    The "origin" service is the service responsible for handling the request from
    the client.

    This model is a component of the "Edge-Request" header.  You should not need to
    interact with this model directly, but rather through the EdgeRequestContext
    interface provided by baseplate.

    Attributes:
     - name: The name of the origin service.


    """

    __slots__ = ("name",)

    def __init__(self, name=None):
        self.name = name

    def read(self, iprot):
        if (
            iprot._fast_decode is not None
            and isinstance(iprot.trans, TTransport.CReadableTransport)
            and self.thrift_spec is not None
        ):
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.name = (
                        iprot.readString().decode("utf-8")
                        if sys.version_info[0] == 2
                        else iprot.readString()
                    )
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin("OriginService")
        if self.name is not None:
            oprot.writeFieldBegin("name", TType.STRING, 1)
            oprot.writeString(self.name.encode("utf-8") if sys.version_info[0] == 2 else self.name)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ["%s=%r" % (key, getattr(self, key)) for key in self.__slots__]
        return "%s(%s)" % (self.__class__.__name__, ", ".join(L))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        for attr in self.__slots__:
            my_val = getattr(self, attr)
            other_val = getattr(other, attr)
            if my_val != other_val:
                return False
        return True

    def __ne__(self, other):
        return not (self == other)


class Geolocation(object):
    """
    Geolocation data from a request to our services that we want to
    propagate between services.

    This model is a component of the "Edge-Request" header.  You should not need to
    interact with this model directly, but rather through the EdgeRequestContext
    interface provided by baseplate.


    Attributes:
     - country_code: The country code of the requesting client.

    """

    __slots__ = ("country_code",)

    def __init__(self, country_code=None):
        self.country_code = country_code

    def read(self, iprot):
        if (
            iprot._fast_decode is not None
            and isinstance(iprot.trans, TTransport.CReadableTransport)
            and self.thrift_spec is not None
        ):
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.country_code = (
                        iprot.readString().decode("utf-8")
                        if sys.version_info[0] == 2
                        else iprot.readString()
                    )
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin("Geolocation")
        if self.country_code is not None:
            oprot.writeFieldBegin("country_code", TType.STRING, 1)
            oprot.writeString(
                self.country_code.encode("utf-8") if sys.version_info[0] == 2 else self.country_code
            )
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ["%s=%r" % (key, getattr(self, key)) for key in self.__slots__]
        return "%s(%s)" % (self.__class__.__name__, ", ".join(L))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        for attr in self.__slots__:
            my_val = getattr(self, attr)
            other_val = getattr(other, attr)
            if my_val != other_val:
                return False
        return True

    def __ne__(self, other):
        return not (self == other)


class Request(object):
    """
    Container model for the Edge-Request context header.

    Baseplate will automatically parse this from the "Edge-Request" header and
    provides an interface that wraps this Thrift model.  You should not need to
    interact with this model directly, but rather through the EdgeRequestContext
    interface provided by baseplate.


    Attributes:
     - loid
     - session
     - authentication_token
     - device
     - origin_service
     - geolocation

    """

    __slots__ = (
        "loid",
        "session",
        "authentication_token",
        "device",
        "origin_service",
        "geolocation",
    )

    def __init__(
        self,
        loid=None,
        session=None,
        authentication_token=None,
        device=None,
        origin_service=None,
        geolocation=None,
    ):
        self.loid = loid
        self.session = session
        self.authentication_token = authentication_token
        self.device = device
        self.origin_service = origin_service
        self.geolocation = geolocation

    def read(self, iprot):
        if (
            iprot._fast_decode is not None
            and isinstance(iprot.trans, TTransport.CReadableTransport)
            and self.thrift_spec is not None
        ):
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRUCT:
                    self.loid = Loid()
                    self.loid.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.session = Session()
                    self.session.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.authentication_token = (
                        iprot.readString().decode("utf-8")
                        if sys.version_info[0] == 2
                        else iprot.readString()
                    )
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRUCT:
                    self.device = Device()
                    self.device.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRUCT:
                    self.origin_service = OriginService()
                    self.origin_service.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRUCT:
                    self.geolocation = Geolocation()
                    self.geolocation.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin("Request")
        if self.loid is not None:
            oprot.writeFieldBegin("loid", TType.STRUCT, 1)
            self.loid.write(oprot)
            oprot.writeFieldEnd()
        if self.session is not None:
            oprot.writeFieldBegin("session", TType.STRUCT, 2)
            self.session.write(oprot)
            oprot.writeFieldEnd()
        if self.authentication_token is not None:
            oprot.writeFieldBegin("authentication_token", TType.STRING, 3)
            oprot.writeString(
                self.authentication_token.encode("utf-8")
                if sys.version_info[0] == 2
                else self.authentication_token
            )
            oprot.writeFieldEnd()
        if self.device is not None:
            oprot.writeFieldBegin("device", TType.STRUCT, 4)
            self.device.write(oprot)
            oprot.writeFieldEnd()
        if self.origin_service is not None:
            oprot.writeFieldBegin("origin_service", TType.STRUCT, 5)
            self.origin_service.write(oprot)
            oprot.writeFieldEnd()
        if self.geolocation is not None:
            oprot.writeFieldBegin("geolocation", TType.STRUCT, 6)
            self.geolocation.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ["%s=%r" % (key, getattr(self, key)) for key in self.__slots__]
        return "%s(%s)" % (self.__class__.__name__, ", ".join(L))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        for attr in self.__slots__:
            my_val = getattr(self, attr)
            other_val = getattr(other, attr)
            if my_val != other_val:
                return False
        return True

    def __ne__(self, other):
        return not (self == other)


class Error(TException):
    """
    Attributes:
     - code: A code describing the general nature of the error.
    This should be specified for all errors. This field uses
    the i32 type instead of the ErrorCode type in order to give
    developers an escape hatch to define their own error codes.
    Developers should do their best to avoid defining a custom
    error code. Developers should use a value higher than 1000
    when defining custom codes.
     - message: A human-readable error message. It should both explain the error
    and offer an actionable resolution to it, if applicable. It should
    be safe to desplay this message in a user-facing client.
     - details: A map of additional error information. This is most useful
    when there is a validation error. The server may use this map
    to return multiple errors. This should be safe for clients to
    display. Example:
        {
            "post.title": "This field is too long.",
            "post.kind": "This field is required."
        }

    """

    __slots__ = (
        "code",
        "message",
        "details",
    )

    def __init__(
        self, code=None, message=None, details=None,
    ):
        self.code = code
        self.message = message
        self.details = details

    def read(self, iprot):
        if (
            iprot._fast_decode is not None
            and isinstance(iprot.trans, TTransport.CReadableTransport)
            and self.thrift_spec is not None
        ):
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.code = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.message = (
                        iprot.readString().decode("utf-8")
                        if sys.version_info[0] == 2
                        else iprot.readString()
                    )
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.MAP:
                    self.details = {}
                    (_ktype1, _vtype2, _size0) = iprot.readMapBegin()
                    for _i4 in range(_size0):
                        _key5 = (
                            iprot.readString().decode("utf-8")
                            if sys.version_info[0] == 2
                            else iprot.readString()
                        )
                        _val6 = (
                            iprot.readString().decode("utf-8")
                            if sys.version_info[0] == 2
                            else iprot.readString()
                        )
                        self.details[_key5] = _val6
                    iprot.readMapEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin("Error")
        if self.code is not None:
            oprot.writeFieldBegin("code", TType.I32, 1)
            oprot.writeI32(self.code)
            oprot.writeFieldEnd()
        if self.message is not None:
            oprot.writeFieldBegin("message", TType.STRING, 2)
            oprot.writeString(
                self.message.encode("utf-8") if sys.version_info[0] == 2 else self.message
            )
            oprot.writeFieldEnd()
        if self.details is not None:
            oprot.writeFieldBegin("details", TType.MAP, 3)
            oprot.writeMapBegin(TType.STRING, TType.STRING, len(self.details))
            for kiter7, viter8 in self.details.items():
                oprot.writeString(kiter7.encode("utf-8") if sys.version_info[0] == 2 else kiter7)
                oprot.writeString(viter8.encode("utf-8") if sys.version_info[0] == 2 else viter8)
            oprot.writeMapEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __str__(self):
        return repr(self)

    def __repr__(self):
        L = ["%s=%r" % (key, getattr(self, key)) for key in self.__slots__]
        return "%s(%s)" % (self.__class__.__name__, ", ".join(L))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        for attr in self.__slots__:
            my_val = getattr(self, attr)
            other_val = getattr(other, attr)
            if my_val != other_val:
                return False
        return True

    def __ne__(self, other):
        return not (self == other)


all_structs.append(Loid)
Loid.thrift_spec = (
    None,  # 0
    (1, TType.STRING, "id", "UTF8", None),  # 1
    (2, TType.I64, "created_ms", None, None),  # 2
)
all_structs.append(Session)
Session.thrift_spec = (None, (1, TType.STRING, "id", "UTF8", None))  # 0  # 1
all_structs.append(Device)
Device.thrift_spec = (None, (1, TType.STRING, "id", "UTF8", None))  # 0  # 1
all_structs.append(OriginService)
OriginService.thrift_spec = (None, (1, TType.STRING, "name", "UTF8", None))  # 0  # 1
all_structs.append(Geolocation)
Geolocation.thrift_spec = (None, (1, TType.STRING, "country_code", "UTF8", None))  # 0  # 1
all_structs.append(Request)
Request.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, "loid", [Loid, None], None),  # 1
    (2, TType.STRUCT, "session", [Session, None], None),  # 2
    (3, TType.STRING, "authentication_token", "UTF8", None),  # 3
    (4, TType.STRUCT, "device", [Device, None], None),  # 4
    (5, TType.STRUCT, "origin_service", [OriginService, None], None),  # 5
    (6, TType.STRUCT, "geolocation", [Geolocation, None], None),  # 6
)
all_structs.append(Error)
Error.thrift_spec = (
    None,  # 0
    (1, TType.I32, "code", None, None),  # 1
    (2, TType.STRING, "message", "UTF8", None),  # 2
    (3, TType.MAP, "details", (TType.STRING, "UTF8", TType.STRING, "UTF8", False), None),  # 3
)
fix_spec(all_structs)
del all_structs
