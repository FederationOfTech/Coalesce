import { mountQuasar } from '@quasar/quasar-app-extension-testing-unit-jest'
import { QBtn, QForm, QInput, QRadio } from 'quasar'
import OrganiserForm from '../create-organiser-form.vue'

const $v = {
  websiteUrl: {
    $dirty: false,
    website: false
  },
  organisationName: {
    $dirty: false
  },
  email: {
    $dirty: false,
    email: false
  },
  $touch: jest.fn()
}

describe('Create Organiser Form', () => {
  it('should be defined', () => {
    const wrapper = mountQuasar(OrganiserForm, {
      quasar: {
        components: {
          QBtn,
          QForm,
          QInput,
          QRadio
        }
      }
    })

    expect(wrapper).toBeTruthy()

    expect(wrapper.exists()).toBe(true)
  })

  it('should have one form with method "post"', () => {
    const wrapper = mountQuasar(OrganiserForm, {
      quasar: {
        components: {
          QBtn,
          QForm,
          QInput,
          QRadio
        }
      }
    })

    expect(wrapper.attributes('method')).toBe('post')
  })

  describe('methods ::', () => {
    describe('isformValid ::', () => {
      let touchSpy

      beforeEach(() => {
        touchSpy = jest.spyOn($v, '$touch')
      })

      afterEach(() => {
        jest.clearAllMocks()
      })

      it('should call `.touch()`', () => {
        const wrapper = mountQuasar(OrganiserForm, {
          quasar: {
            components: {
              QBtn,
              QForm,
              QInput,
              QRadio
            }
          },
          mount: {
            mocks: { $v }
          }
        })

        wrapper.vm.isFormValid()

        expect(touchSpy).toBeCalled()
      })

      it('should return `true` if `$v` is valid', () => {
        $v.$invalid = false

        const wrapper = mountQuasar(OrganiserForm, {
          quasar: {
            components: {
              QBtn,
              QForm,
              QInput,
              QRadio
            }
          },
          mount: {
            mocks: { $v }
          }
        })

        expect(wrapper.vm.isFormValid()).toBeTruthy()
      })

      it('should return `false` if `$v` is invalid', () => {
        $v.$invalid = true

        const wrapper = mountQuasar(OrganiserForm, {
          quasar: {
            components: {
              QBtn,
              QForm,
              QInput,
              QRadio
            }
          },
          mount: {
            mocks: { $v }
          }
        })

        expect(wrapper.vm.isFormValid()).toBeFalsy()
      })
    })

    describe('onFormSubmit', () => {
      let isFormValidSpy

      beforeEach(() => {
        isFormValidSpy = jest.spyOn(OrganiserForm.methods, 'isFormValid')
      })

      it('should exist', () => {
        const wrapper = mountQuasar(OrganiserForm, {
          quasar: {
            components: {
              QBtn,
              QForm,
              QInput,
              QRadio
            }
          },
          mount: {
            mocks: { $v }
          }
        })

        expect(wrapper.vm.onFormSubmit).toBeDefined()
      })

      describe('When invoked', () => {
        describe('And the form is not valid', () => {
          it('should not call `createOrganiser`', async () => {
            isFormValidSpy.mockReturnValue(false)
            const wrapper = mountQuasar(OrganiserForm, {
              quasar: {
                components: {
                  QBtn,
                  QForm,
                  QInput,
                  QRadio
                }
              },
              mount: {
                mocks: { $v }
              }
            })

            const createOrganiserSpy = jest.spyOn(wrapper.vm, 'createOrganiser')

            await wrapper.vm.onFormSubmit()

            expect(createOrganiserSpy).not.toHaveBeenCalled()
          })
        })
        describe('And the form is valid', () => {
          it('should call `createOrganiser`', async () => {
            isFormValidSpy.mockReturnValue(true)
            const wrapper = mountQuasar(OrganiserForm, {
              quasar: {
                components: {
                  QBtn,
                  QForm,
                  QInput,
                  QRadio
                }
              },
              mount: {
                mocks: { $v }
              }
            })

            const createOrganiserSpy = jest.spyOn(wrapper.vm, 'createOrganiser')

            await wrapper.vm.onFormSubmit()

            expect(createOrganiserSpy).toHaveBeenCalled()
          })
        })
      })
    })
  })
})
